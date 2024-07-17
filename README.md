# Using Cell Nuclei Characteristics to Diagnose Breast Cancer through Supervized Machine Learning

In this notebook, we will be aiming to classify breast cancer cells as benign or malignant using physical characteristics of their cell nuclei. The classification algorithm that will be used are supervized machine learning models, which will be deployed in a web-app.

# Running the File
To run this, download the whole repository and then run app.py. At the terminal, click on the server number to see the link for the model. It is preceded by "Running on." 
Input the data into the website and then the website will return whether the cell is benign or malignant.

# Data
The continuous data are marked with 1, 2, or 3, indicating their data type:
* 1: mean
* 2: standard error
* 3: worst (mean of the three largest values of the features computed for the images)

# Data Sources
The data is taken from: https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic.

# Goals
Currently, this is still in the development stages. The following are still not accomplished.
* 1: Check if the model is not overfitting.
* 2: Deploy the model using Flask, HTML, and CSS.
