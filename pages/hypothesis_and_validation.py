# Import streamlit
import streamlit as st

# Page title and text
def show():
    st.title("Project Hypothesis and Validation")
    
    st.info('''
    -We suspect that powdery mildew infected cherry leaves have visible differences 
    from healthy ones. 
    
    -One of the most characteristic signs of powdery mildew is the
    presence of a white, powdery or dusty substance on the surface of the affected leaves.
    ''')

    
    st.success('''
    This hypothesis was validated by:

    * Computing Average Image, Variable Images and Difference 
    between Averages Images from both healthy and powdery-mildew classes. 
    * The montage images show:
    
        -The powdery growth can cover the entire leaf and often 
        resembles a coating of flour or talcum powder, which Healthy cherry leaves do not have.
        
        -Infected cherry leaves may develop yellow or brown spots or patches, particularly on the 
        areas covered by the powdery growth.
        
        -Infected leaves can appear in curling, twisting, or other abnormal leaf shapes. 
        Healthy cherry leaves typically have a more uniform and symmetrical appearance.
    
    * The average images of both classes show very different shapes, which could prove that infected 
    cherry leaves may exhibit a signs of distortion or malformation.  
    ''')