import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
# from utlis.detective_model.evaluate import load_test_evaluation
import joblib

# Page title and text
def show():
    st.title("Model Performance Metrics")
    version = 'v1-mildew'

    st.write("### Labels distribution on Train, Validation and Test Set ")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution among Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model Learning history")
    st.info(f'''
        -The model was trained over 50 epochs, achieving the below loss and accuracy learning curve on training
        and validation set respectively.
        
        -A nice learning trendy progress indicates a normal fit model staring with high loss and low accuracy 
        (train_loss: 0.3076 - train_accuracy: 0.8509, val_loss: 0.1622 - val_accuracy: 0.9714)  
        end up with loss nearly to zero and accuracy close to 1 (train_loss: 0.0160 - accuracy: 0.9942, val_loss: 0.0107 - val_accuracy: 1.0000). ''')
    
    model_evaluation = plt.imread(f"outputs/{version}/model_training_metrics3.png")
    st.image(model_evaluation, caption='Model Training Evaluation')
    st.write("---")

    st.write("### Generalized Performance on Test Set") 
    # Create a layout with a horizontal alignment and their tops aligned
    col1, col2 = st.beta_columns(2)   
    
    # Load the evaluation data
    evaluation_data = pd.DataFrame(joblib.load(f'outputs/{version}/mildew_model_evaluation3.pkl'), index=['Loss', 'Accuracy'])

    col2.dataframe(evaluation_data, height=200)
    
    model_evaluation_bar = plt.imread(f"outputs/{version}/model_evaluation_metrics.png")
    
    col1.image(model_evaluation_bar)
    st.write('<style>div.row-widget.stImage {height: 400px;}</style>', unsafe_allow_html=True)
    st.write("---")
    
    st.markdown('### Confusion Matrix and Classification Report on Test Dataset')
    st.info(f'''
            Both confusion matrix and classification analysis showed a higher prediction rate of 100% in powdery mildew class
            and lower accuracy rate in healthy class. Which is preferable as the model setting and training''')
    
    st.success('The confusion matrix from model evaluation on the test data.')
    IMAGE_PATH ="outputs/{version}"
    cm_test = plt.imread(f"outputs/{version}/confusion_matrix_test.png")
    st.image(cm_test, caption='Confusion matrix - test data', use_column_width=True)
    
    st.success('The classification reports from model evaluation on test data.')
    cr_test = pd.read_csv((f'outputs/{version}/classification_report_test.csv'))
    st.table(cr_test)
