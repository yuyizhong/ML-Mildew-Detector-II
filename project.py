import streamlit as st
from pages import project_summary, data_visualization, cherry_leaf_health_detection, hypothesis_and_validation, model_performance_metrics

# Add custom CSS styles
st.markdown(
    """
    <style>
        .title {
            color: blue;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a top bar for navigation
st.markdown("<h1 class='title'>Cherry Leave Mildew Detector</h1>", unsafe_allow_html=True)

# Create a sidebar to navigate between pages
page = st.selectbox("Select a Page", ["Project Summary", "Cherry Leaf Visualization", "Cherry Leaf Powdery_mildew Detection", "Project Hypothesis and Validation", "Model Performance Metrics"])

# Define the page content functions
page_functions = {
    "Project Summary": project_summary.show,
    "Cherry Leaf Visualizer": data_visualization.show,
    "Cherry Leaf Health Detection": cherry_leaf_health_detection.show,
    "Project Hypothesis and Validation": hypothesis_and_validation.show,
    "Model Performance Metrics": model_performance_metrics.show
}

# Based on the selected page, display the corresponding content
if page in page_functions:
    page_functions[page]()