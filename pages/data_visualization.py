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
from PIL import Image

# Page title and text


def show():
    """
    Show the Cherry Leaf Visualization page with different options.
    """
    st.title("Cherry Leaf Visualization")
    st.info('''
        This page is to answer the client's first business requirement
        to carry out an analysis on:

        * average images and variability images for each class
          (healthy or powdery mildew),
        * the differences between average healthy and average powdery
          mildew cherry leaves,
        * an image montage for each class. ''')

    version = 'v1-mildew'

    selected_option = st.radio("Select an option:", [
        "Average and variability image by class",
        "Differences of average infected and healthy leaves",
        "Image Montage by Class"
    ])

    if selected_option == "Average and variability image by class":
        show_average_images(version)

    if selected_option == "Differences of average infected and healthy leaves":
        show_difference_between_average_images(version)

    if selected_option == "Image Montage by Class":
        create_image_montage('inputs/mildew_dataset/cherry-leaves/validation')


def show_average_images(version):
    """
    Show average and variability images.
    """
    avg_powdery_mildew = plt.imread(
        f"outputs/{version}/avg_var_powdery_mildew.png")
    avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")

    st.success('''
    The average and variability images indicate the color and shape
    difference between two labels, and the healthy class seems less
    variable in shapes.
    ''')
    st.image(avg_powdery_mildew,
             caption='Powdery Mildew contained cherry leaves'
             '- Average and Variability')
    st.image(
        avg_healthy, caption='Healthy cherry leaves - Average and Variability'
    )
    st.write("---")


def show_difference_between_average_images(version):
    """
    Show differences between average infected and average healthy leaves.
    """
    diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

    st.success('''
        This study shows intuitive differences in shapes and slightly
        in pigmentations.
    ''')
    st.image(diff_between_avgs, caption='Difference between average images')


def create_image_montage(dir_path):
    """
    Create an image montage.
    """
    labels = ['powdery_mildew', 'healthy']
    label_to_display = st.selectbox(
        label="Select cherry leaf class", options=labels, index=0)

    if st.button("Create/Refresh Montage"):
        nrows, ncols = 4, 4
        create_and_display_image_montage(
            dir_path, label_to_display, nrows, ncols)

    st.write("---")


def create_and_display_image_montage(
    dir_path, label_to_display, nrows, ncols, figsize=(55, 50)
):

    """
    Create and display an image montage.
    """
    sns.set_style("white")
    labels = ['powdery_mildew', 'healthy']
    if label_to_display.lower() not in [label.lower() for label in labels]:
        st.error("The selected label doesn't exist.")
        st.write(f"The existing options are: {labels}")
        return

    images_list = os.listdir(os.path.join(dir_path, label_to_display))
    if nrows * ncols >= len(images_list):
        st.error(
            "Decrease nrows or ncols to create your montage. "
            "There are {len(images_list)} images in your subset,"
            "but you requested a montage with {nrows * ncols} spaces."
        )
        return

    img_idx = random.sample(images_list, nrows * ncols)
    plot_idx = list(itertools.product(range(nrows), range(ncols)))
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

    # Set smaller image size
    new_image_size = (70, 70)

    for x in range(nrows * ncols):
        img_path = os.path.join(dir_path, label_to_display, img_idx[x])
        img = imread(img_path)

        # Resize the image to 80x80
        img = Image.fromarray(img)
        img = img.resize(new_image_size)

        img_shape = img.size

        axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
        axes[plot_idx[x][0], plot_idx[x][1]].set_title(
            f"Width {img_shape[0]}px x Height {img_shape[1]}px")
        axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
        axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])

    plt.tight_layout()
    st.pyplot(fig=fig)


if __name__ == "__main__":
    show()
