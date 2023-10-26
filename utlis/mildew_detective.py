
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
import joblib


def resize_input_image(img, version):
    """
    Resize an image to a specified shape.

    """
    # Load the target image shape from a file
    image_shape = joblib.load(f"outputs/{version}/image_shape.pkl")

    # Resize the input image using the specified shape
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.BILINEAR)

    # Convert the resized image to a NumPy array and normalize it
    my_image = np.expand_dims(img_resized, axis=0)/255

    return my_image


def load_model_and_predict(my_image, version):
    """
    Perform ML prediction with live images
    """

    model = load_model(f"outputs/{version}/mildew_detecting_model.h5")

    pred_prob = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'healthy': 0, 'powdery_mildew': 1}.items()}
    pred_class = target_map[pred_prob > 0.97]
    prob = (pred_prob * 100).round(2)

    if pred_class == target_map[0]:
        pred_prob = 1 - pred_prob
        prob = pred_prob.round(3)*100
    st.write(
        f"The predictive analysis indicates the sample leave **{prob}%** "
        f"is **{pred_class.lower()}**")

    return pred_prob, pred_class

# The below function is modified from CI walk through project


def plot_classification_probabilities(pred_prob, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'healthy': 0, 'powdery_mildew': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_prob
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_prob
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Detection Result'] = prob_per_class.index

    # Define colors for the Pie Chart
    colors = {'healthy': 'green', 'powdery_mildew': 'blue'}

    fig = px.pie(prob_per_class, names='Detection Result', values='Probability',
                 color='Detection Result',
                 color_discrete_map=colors)
    st.plotly_chart(fig)
