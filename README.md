# Big-Data-Applications-Project

Big Data Applications Project 2021

Group Members:

- Florian SHONG GEU
- Jean Brice KOUADIO

## Introduction

The first step of the project is to create three classification machine learning models, using three different methods:
- Random Forest
- XGBoost
- Gradient Boosting

However, the goal of this project isn't just to create three machine learning models. Indeed, these models' accuracies aren't very important, because the real goal is to implement
multiple tools into the project, in order to make the project more understandable for everyone.
The tools to be used are:
- Git
- Conda environment
- Mlflow
- SHAP

The data used is from kaggle, it's a datasrt about credit risk. We could only upload the test dataset on the git repository, as the train one was unfortunately too big to be uploaded.

## Structuration

The main file is project.py
We decided to not use multiple branches in the Git repository, as we thought it wasn't necessary.
For the project documentation, we used Sphinx.

## Models

For the models implementation, we let the choice to the user for the model, and also for the number of estimators used.
After that, the program will create the model and predict values based on the user's choices. All models' data are given to Mlflow.
Some metrics are calculated using scikit-learn, in order to see what model and what parameters are the most efficient.

The mlflow result is:

![image](https://user-images.githubusercontent.com/93647151/143055651-89d26cec-5b23-443f-8655-f4504043234e.png)

With this, we can compare our different models to see which ones are the most accurate

## Shap

To obtain more explainability about the trained models, we use Shap.
With Shap we can provide more information about the models and its parameters (for example what parameters are the most important for the prediction).

The obtained result is:

![image](https://user-images.githubusercontent.com/93647151/143055347-bca39a96-d6a4-4ba0-b293-6101eb59a10f.png)

On the chart, we can see what parameters are the most important for our models (EXT_SOURCE 1, 2 and 3)


