# Cherry Leave Mildew Detector
An Machine learning Image classifier project to detect a particular cherry leaves health condition by using convolutional neural networks (CNN) to map the relationships between the features and the labels.

# Table of Contents

1. [Dataset Content](#dataset-content)
2. [Business Requirements](#business-requirements)
3. [Hypothesis and Validation](#hypothesis-and-validation)
4. [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
   - [Epics](#epics)
   - [User Stories](#user-stories)
      1. [Data Collection and Preparation](#data-collection-and-preparation)
      2. [Data Visualization](#data-visualization)
      3. [Model Training, Optimization, and Evaluation](#model-training-optimization-and-evaluation)
      4. [Dashboard Planning, Designing, and Development and Deployment](#dashboard-planning-designing-and-development-and-deployment)
5. [ML Business Case](#ml-business-case)
6. [Dashboard Design (Streamlit App User Interface)](#dashboard-design-streamlit-app-user-interface)
   - [Page 1: Project Summary](#page-2-project-summary)
   - [Page 2: Data Visualization](#page-3-data-visualization)
   - [Page 3: Cherry leave health detection](#page-4-cherry-leave-health-detection)
   - [Page 4: Hypothesis and Validation](#page-5-hypothesis-and-validation)
   - [Page 5: Model Performance Metrics](#page-6-model-performance-metrics)
7. [Deployment](#deployment)
8. [Main Data Analysis & Machine Learning Libraries](#main-data-analysis--machine-learning-libraries)
9. [Run locally](#run-locally)
10. [Credits](#credits)

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
__Hypothesis__: powdery mildew infected cherry leaves have visible differences 
    from healthy ones.
__How to validate__: Conduct Average Image, Variable Images and Difference 
    between Averages Images Study of both healthy and powdery-mildew classes.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
### Epics:

- __Data collection and preparation__
- __Data visualization__
- __Model training, optimization and evaluation__
- __Dashboard planning, designing, and development and deployment__
- __API Development and deployment__

### User stories:

#### Data collection and preparation

1. **User Story:** As a developer, I can source and acquire the data to create a reliable and well-prepared dataset for the project.
   - **Task:** Download the dataset, extract, clean and prepare the relevant data, and save it at structured repository folder.

#### Data Visualization

1. **User Story:** As a developer, I can generate informative visualizations to understand the data, providing valuable insights to the client.
   - **Task:** Choose appropriate visualization techniques, generate visualizations and save them as outputs.

2. **User Story:** As a developer, I can integrate data visualizations into the dashboard for user-friendly data exploration.
   - **Task:** Design the layout of the data visualization page and implement interactive features.

#### Model Training, Optimization, and Evaluation

1. **User Story:** As a developer, I can set up model and explore the optimal hyperparamaters to train the model in a set range of parameters.
   - **Task:** Setup Model structure using techniques such as Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization and optimizers.

2. **User Story:** As a developer, I can train and fine-tune the machine learning model based on the optimal hyperparameters found to achieve an agreed performance criteria a 97% accuracy.
   - **Task:** Further define model architecture and implement a function to build the model based on the found optimal hyperparameters.

3. **User Story:** As a developer, I can evaluate my models performance using a variety of metrics.
	- **Task:** Perform model evaluation using a Machine Learning library, visually represent the results and save the visualizations.

4. **User Story:** As a user, I can access model evaluation results, helping me understand the model's performance.
   - **Task:** Provide a user interface at dashboard page for accessing model evaluation reports.

#### Dashboard Planning, Designing, and Development

1.  **User Story:** As a developer, I can implement Streamlit features to answer the business requirements, making it interactive and user-friendly. 
	-  **Task:** Develop and integrate interactive Streamlit features and functionalities into the dashboard.

2. **User Story:** As a user, I can access and interact with the Streamlit features, enabling me to navigate through the project, explore data visualizations, and make live predictions on the model.
	-  **Task:** Provide navigation options, interactive data exploration features and a page for making live predictions with a way to download sample images for making predictions.

#### Dashboard Deployment and Release

1.  **User Story:** As a developer, I can deploy the Streamlit dashboard, ensuring it is accessible to users.
2.  **User Story:** As a user, I can access the dashboard online and navigate the visualizations and make live predictions at any time any where when internet is available. 
	- **Task:** Deploy the streamlit app to Heroku and ensure the dashboard is accessible online.


## ML Business Case
- We want to deliver an ML model to detect whether a cherry leaf is healthy or contains powdery mildew. The target variable is categorical and contains 2-classes. We consider a  **classification model** and use Neural Networks to map the relationships between the features and the labels. It is a supervised model, a 2-class, single-label, classification model which produces output: 0 (healthy) or 1 (powdery_mildew).
- Our aim is to achieve the performance criteria  of accuracy of at least 97%
- Our ideal outcome is to provide our client with a reliable instant prediction solution and reduce the risk of supplying the market with a product of compromised quality.


## Dashboard Design (Streamlit App User Interface)

### Page 1: Project Summary

    - Quick project summary providing background information about the project and its importance.
    - General information about the problem and the available dataset.
    - Business requirements

### Page 2: Cherry Leaf Visualizer

Addressing Business Requirement 1: Differentiating healthy cherry leaves from powdery mildew.
Components:

    - Show average and variability images for each class (healthy and powdery mildew).
    - Display the differences between average healthy and average powdery mildew cherry leaves.
    - Create an image montage for each class.

Visual representations of the average images, differences, and image montages for better understanding.

### Page 3: Cherry Leaf Health Detection

Addressing Business Requirement 2: Predicting if a cherry leaf is healthy or contains powdery mildew.
Components:

    - Link to download a set of cherry leaf images for live prediction (from the provided dataset).
    - User Interface with a file uploader widget for uploading multiple cherry leaf images.
    - Display of uploaded images and prediction statements (healthy or powdery mildew) with associated probabilities.
    - A table showing the image name and prediction results.
    - Download link to download the prediction results.

### Page 4: Project Hypothesis and Validation
    - Provides information on project hypotheses and their validation.
    - Separate blocks for each hypothesis with conclusions and validation details.

### Page 5: Model Performance Metrics
    - Display of machine learning model performance metrics.
    - Label frequencies for the train, validation, and test datasets.
    - Model history showing accuracy and loss curves during training.
    - Model evaluation results on test data
    - Confusion Matrix and Classification analysis on test data


## Deployment
### Heroku

* The App live link is: https://ml-mildew-detector-97c034e200fa.herokuapp.com/

**Steps before heroku deployment:**

* Set the runtime.txt Python version python-3.8.14 to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* Downgrade Heroku version from 22 to Heroku-20 with the below steps:
   - Login to Heroku with this command:
     Heroku login -i
   - Then:
     heroku stack:set heroku-20 -a <app name>
     Replace <app name> with your app name for Heroku.

**The project was then deployed to Heroku using the following steps**.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select the repository name and click Search. Once it is found, click Connect.
4. Select branch ML to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries

__Main Data analysis libraries used__:

- Numpy
	- For performing calculations on large amounts of data efficiently, mainly pixel data in this case
	- Normalizing pixel data
	- Calculating means and standard deviations
	- Base for other data analysis and ML libraries
- Pandas
	- Mainly for pandas DataFrame's for easy management of large data (sampling, shuffling, concatenation etc.)
- Matplotlib & Seaborn
	- For plotting and visualization of data
	- Showing images from pixel data
	- Metric plots & Histograms

__Main Machine Learning libraries used:__

- TensorFlow & Keras
	- Image augmentation
	- Model loading
	- Defining model architecture
	- Training model
	- One-hot encoding
	- tensorflow.data.Datset API
- Scikit Learn
	- Hyperparameter optimization using GridSearchCV
	- Generating confusion matrixes & classification reports
- OpenCV
	- Reading images pixel data as NumPy arrays
	- Resizing images

__Steamlit was used to build the interface to deliver the analysis results and ML model to users__

## Credits 

- [Churnometer repo by Code Institute](https://github.com/Code-Institute-Solutions/churnometer#readme): For the Readme template/structure.

- [Streamlit documentation](https://docs.streamlit.io/): For getting the web app up and running.

- This project was also inspired by Code Institute Walkthrough project Malaria Detector 
