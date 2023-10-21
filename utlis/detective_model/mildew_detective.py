import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
import joblib


def plot_classification_probabilities(class_probabilities, class_labels, title="Prediction Probabilities"):
    """
    Plot classification prediction probabilities.

    Args:
        class_probabilities (list): List of class probabilities.
        class_labels (list): List of class labels.
        title (str, optional): Title for the plot. Default is "Prediction Probabilities".
    """
    # Create a DataFrame from class probabilities and labels
    prob_per_class = pd.DataFrame({
        'Class': class_labels,
        'Probability': class_probabilities
    })

    # Create a Plotly bar chart
    fig = px.bar(
        prob_per_class,
        x='Class',
        y='Probability',
        title=title,
        range_y=[0, 1],
        labels={'Probability': 'Probability'},
        width=600,
        height=300,
        template='seaborn'
    )

    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Resize an image to a specified shape.

    Args:
        img (PIL.Image.Image): The input image to be resized.
        version (str): The version identifier for loading image shape.
    """
    # Load the target image shape from a file
    image_shape = joblib.load(f"outputs/{version}/image_shape.pkl")

    # Resize the input image using the specified shape
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)

    # Convert the resized image to a NumPy array and normalize it
    my_image = np.expand_dims(np.array(img_resized) / 255.0, axis=0)

    return my_image


def load_model_and_predict(my_image, version):
    """
    Perform ML prediction with live images
    """

    model = load_model(f"outputs/{version}/mildew_detecting_model.h5")

    pred_prob = model.predict(my_image)[0, 0]

    target_map = {v: k for k, v in {'powdery-mildew': 0, 'healthy': 1}.items()}
    pred_class = target_map[pred_prob > 0.97]
    if pred_class == target_map[0]:
        pred_prob = 1 - pred_prob

    st.write(
        f"The predictive analysis indicates the sample leave is "
        f"**{pred_class.lower()}** infected.")

    return pred_proba, pred_class