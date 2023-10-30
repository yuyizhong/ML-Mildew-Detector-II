import streamlit as st
from pages import project_summary, data_visualization, cherry_leaf_health_detection, hypothesis_and_validation, model_performance_metrics

# Add custom CSS styles
st.markdown(
    """
    <style>
        .title {
            color: blue;
        }
        /* Style the selectbox label text */
        .dropdown-label {
            color: green;
            font-size: 20px;
        }
        
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a top bar for navigation
st.markdown("<h1 class='title'>Cherry Leave Mildew Detector</h1>", unsafe_allow_html=True)

# Create a dropdown menu to navigate between pages

st.markdown("<span class='dropdown-label'>Select a Page:</span>", unsafe_allow_html=True)
page = st.selectbox("",  ["Project Summary", "Cherry Leaf Visualization", "Cherry Leaf Health Detection", "Project Hypothesis and Validation", "Model Performance Metrics"], key="selectbox")

# Define the page content functions
page_functions = {
    "Project Summary": project_summary.show,
    "Cherry Leaf Visualization": data_visualization.show,
    "Cherry Leaf Health Detection": cherry_leaf_health_detection.show,
    "Project Hypothesis and Validation": hypothesis_and_validation.show,
    "Model Performance Metrics": model_performance_metrics.show
}

# Based on the selected page, display the corresponding content
if page in page_functions:
    page_functions[page]()