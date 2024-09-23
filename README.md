# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the Cherry Leaves project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly okay to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

1. Log into your cloud IDE with your GitHub account.

1. On your Dashboard, click on the New Workspace button

1. Paste in the URL you copied from GitHub earlier

1. Click Create

1. Wait for the workspace to open. This can take a few minutes.

1. Open a new terminal and `pip3 install -r requirements.txt`

1. Open the jupyter_notebooks directory, and click on the notebook you want to open.

1. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace, so it will be Python-3.8.18 as installed by our template. To confirm this, you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, then you can create a new one with _Regenerate API Key_.

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- A leaf affected by powdery mildew exhibits several features that can differentiate them from healthy ones. Typical characteristics of infected leaf include display of particular marks/signs and morphological changes.  For example, leaves being light in color and roughly-circular. Additional indistinguishable feature is the presence of powder-looking patches on young and susceptible leaves. 

- An Image Montage can define a typical powdery mildew leaf based on the presence of fine white marks. On the other hand, studies based on Average Image, Variability Image, and Difference between Averages didn't reveal any clear pattern to differentiate leaves.

- The ML model will be able to distinguish between a healthy and an infected cherry leaf with at least 97% accuracy.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

## Rationale to map the business requirements to the Data Visualizations and ML tasks


### Business Requirement 1: Data visualisation

- As a  client I want to display the "mean" and "standard deviation" of healthy cherry leaf images and cherry leaves that contain powdery mildew, so that I can visually differentiate both the leaves

- As a client I want to display the difference between an average cherry leaf that is healthy and a cherry leaf infected with powdery mildew, enabling to visually distinguish between them.

- As a client I want to display an image montage for cherry leaves that are healthy and cherry leaves that contain powdery mildew, so that I can visually differentiate cherry leaves.


### Business Requirement 2: Classification of images

- As a client I want to predict if a given cherry leaf is healthy or contains powdery mildew.

- As a client I want to build a ML model and generate reports.


## ML Business Case


- From the dataset we want to develop a supervised binary classification machine learning model to accurately predict the presence of powdery mildew on cherry leaves. The goal is to streamline the disease detection process, reducing manual labor and enhancing the efficiency of cherry plantation management.

- Currently the disease is identified manually and it takes around 30 minutes for each tree. The process is very time-consuming and it is not scalable.

- The model output is defined as a flag, indicating if the leaf contains any feature that can show that the tree is infected. The staff of the plantation will take a picture of some leaves of the tree and upload them to the App. The prediction is made on the fly.

- The success metric has been set at 97% accuracy on the test set or above.

- The company will benefit by improving the quality of their product.

- The training data can be found from Kaggle. This contains 4208 Images. All images are uniformed at (256,256,256,3). To ensure the performance is not affected we will reduce the image shape to something around 100x100.

## Dashboard Design change !!!!!

- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs  change !!!!!

- 

## Deployment

### Heroku

- The App live link is: `https://cherry-leaves-detector-4bfba1113616.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

### Languages

Python

### Frameworks and other technologies

1. **Git**: Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

2. **GitHub:** GitHub is used to store the projects code after being pushed from Git.

3. **Balsamiq**: Balsamiq is used to create wireframes.

4. **Heroku**: It is a container-based cloud platform used for deployment.

### Data Analysis and Machine Learning Libraries 

Following are the list of libraries used in the project

1. **Numpy**: A powerful Python library for working with arrays and matrices, offering efficient mathematical operations and linear algebra functions.

2. **Pandas**: A versatile data analysis tool that provides structures like DataFrames for organizing and manipulating data, making it easy to clean, explore, and analyze datasets.

3. **Matplotlib**:  A flexible plotting library that allows you to create various types of visualizations like line plots, scatter plots, histograms, and bar charts to explore and understand data.

4. **Seaborn**: A higher-level data visualization library built on top of Matplotlib, offering a more consistent and aesthetically pleasing style, making it easier to create visually appealing plots.

5. **Plotly**: It is an interactive, open-soource, and browser-based gra6.	Tensorflow: It is an open-sourec machine learning platform focused on deep neural networks.phing library. Used to create visualisations within Jupyter notebooks to present the data.

6. **Tensorflow**: A popular open-source machine learning framework that is widely used for building and training deep neural networks, making it a powerful tool for tasks like image recognition, natural language processing, and predictive modeling.

7. **Shutil**: Used form file copying and removal.

8. **Streamlit**: It is used to create web apps for data science and machine learning.

9. **Joblib**: It is a set of tools  to provide lightweighting pipelining in Python.

10. **PIL**:  A library that adds support for working with images in Python, allowing you to open, manipulate, and save images in various formats.

## Credits

- [Code Institute Malaria Walk Through Project](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/) : The code and design was taken from  Code-Institute-Org/WalkthroughProject01. It helped me alot with understanding the concepts of Machine-learning and i only changed some small parts.

- [GyanShashwat1611/WalkthroughProject01](https://github.com/GyanShashwat1611/WalkthroughProject01) github repository was used for code reference and assistance for in the jupyter notebook set up and for the app page design.

- [alerebal/Powdery Mildew] (https://github.com/Code-Institute-Submissions/milestone-project-mildew-detection-in-cherry-leaves.git) in Cherry Leaves Detector: Readme guidance

### Content

- Streamlit documentation

- Code Institute Lecture and Videos 
