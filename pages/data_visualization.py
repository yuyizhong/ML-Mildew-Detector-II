# Import libraries
import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random

# Page title and text
def show():
    st.title("Cherry Leaf Visualization")
    st.info("The client is interested in differentiating powdery mildew and healthy cherry leaves.")

    version = 'v1-mildew'
    
    selected_option = st.radio("Select an option:", [
        "Difference between average and variability image",
        "Differences between average infected and average healthy leaves",
        "Image Montage"
    ])

    if st.checkbox("Difference between average and variability image"):
        show_average_images(version)

    if st.checkbox("Differences between average infected and average healthy leaves"):
        show_difference_between_average_images(version)

    if st.checkbox("Image Montage"):
        create_image_montage()

def show_average_images(version):
    avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
    avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

    st.warning(
        "The average and variability images show XXXXX, "
        "but a slight variation in color pigments is observed for both labels."
    )
    st.image(avg_powdery_mildew, caption='Powdery Mildew contained cherry leave - Average and Variability')
    st.image(avg_healthy, caption='Healthy cherry leave - Average and Variability')
    st.write("---")

def show_difference_between_average_images(version):
    diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

    st.warning("This study show intuitive differencesXXXXXXX.")
    st.image(diff_between_avgs, caption='Difference between average images')

def create_image_montage():
    st.write("* To refresh the montage, click on the 'Create Montage' button")
    my_data_dir = 'inputs/mildew_dataset/cherry-leaves'
    labels = os.listdir(os.path.join(my_data_dir, 'validation'))
    label_to_display = st.selectbox(label="Select label", options=labels, index=0)

    if st.button("Create Montage"):
        nrows, ncols = 8, 3
        create_and_display_image_montage(my_data_dir, label_to_display, nrows, ncols)
    st.write("---")

def create_and_display_image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    if label_to_display not in labels:
        st.error("The selected label doesn't exist.")
        st.write(f"The existing options are: {labels}")
        return

    images_list = os.listdir(os.path.join(dir_path, label_to_display))
    if nrows * ncols >= len(images_list):
        st.error(
            "Decrease nrows or ncols to create your montage. "
            f"There are {len(images_list)} images in your subset, but you requested a montage with {nrows * ncols} spaces."
        )
        return

    img_idx = random.sample(images_list, nrows * ncols)
    plot_idx = list(itertools.product(range(nrows), range(ncols)))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

    for x in range(nrows * ncols):
        img_path = os.path.join(dir_path, label_to_display, img_idx[x])
        img = imread(img_path)
        img_shape = img.shape

        axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
        axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
        axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
        axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])

    plt.tight_layout()
    st.pyplot(fig=fig)
