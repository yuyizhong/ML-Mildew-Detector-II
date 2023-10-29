# Import streamlit
import streamlit as st

# Page title and text
def show():
    st.title("Project Summary")

    st.info('''
    __General info__
    * Powdery mildew, a fungal disease that affects many plant species. Our client Farm & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew.
    * The manual verification if a given cherry tree containing powdery mildew takes 30 minutes per employee in each tree.
    * The company has thousands of cherry trees, located on multiple farms across the country. As a result, manual process is not efficient and won't satisfy the business needs.
    * To solve this problem, ML system is developed to detect instantly, using a leaf tree image, if a cherry leave is healthy or has powdery mildew. 
   ''')

    st.success('''
    __Project Dataset__
    * The available dataset contains +4 thousand images taken from the client's crop fields. 
    * The images show healthy cherry leaves and cherry leaves that have powdery mildew.
    ''')

    st.markdown('__Further information can be found on the [projects **README.md** file](https://github.com/yuyizhong/ML-Mildew-Detector-/blob/main/README.md)__')

    st.warning('''
    __Business requirements__
    
    -The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    
    -The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
    ''')