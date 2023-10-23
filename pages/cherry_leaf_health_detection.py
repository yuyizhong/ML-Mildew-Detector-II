# # Import modules
import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

# Page title and text
def show():
    st.title("Cherry Leaf Powdery_mildew Detection")
    
    from utlis.data_process import download_df_as_csv
    from utlis.mildew_detective import (
                                        load_model_and_predict,
                                        resize_input_image,
                                        plot_classification_probabilities
                                        )

   
    st.success('''
        This page is to answer client's second business requirement
        to deliver an ML system that is capable of predicting whether 
        a cherry leaf is healthy or contains powdery mildew. ''')

    st.write('''
        You can download a set of infected and healthy cherry leave images for live prediction
        from [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).
        ''')

    st.write("---")
    
    # Allow users to download images
    LIVE_IMG_DIR = 'https://www.kaggle.com/datasets/codeinstitute/cherry-leaves'
    with open(LIVE_IMG_DIR, 'rb') as f:
        st.download_button('Download Zip', f, file_name='cherry-leaves.zip')
        
    #Upload files
    uploaded_images = st.file_uploader('Upload cherry leaf samples. You may select more than one.',
                                      type='jpg', accept_multiple_files=True)

    if uploaded_images:
        df_report = pd.DataFrame([])

        for image in uploaded_images:
            img_pil = Image.open(image)
            st.info(f"Cherry Leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1-mildew'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_prob, pred_class = load_model_and_predict(resized_img, version=version)
            plot_classification_probabilities(pred_prob, pred_class)

            pred_prob_percentage = f"{pred_prob * 100 :.2f}%"  # Convert probability to percentage
            df_report = df_report.append({"Name": image.name, "Result": pred_class, "Accuracy %": pred_prob_percentage},
                                        ignore_index=True)

        if not df_report.empty:
            # Define custom CSS for the table
            custom_css = """
            <style>
                td {
                    font-size: 14px;
                    text-align: center;
                    border: 2px solid lightgrey;
                }

                th {
                    background-color: lightblue;
                    text-align: center;
                    border: 2px solid lightgrey;
                }
            </style>
            """
            # Display the table with the custom CSS
            st.markdown(custom_css, unsafe_allow_html=True)
            st.write('## Detection Report')
            st.table(df_report)
            st.markdown(download_df_as_csv(df_report), unsafe_allow_html=True)
    else:
        st.error('No files uploaded')