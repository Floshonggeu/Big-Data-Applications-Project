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

## Structuration

After creating a Git repository and granting access to everyone that needed it, we decided to start computing models on Jupyter Lab in a Conda environment.
We decided to not use multiple branches in the Git repository, as we thought it wasn't necessary.
For the project documentation, we used Sphinx.

## Models

For the models implementation, we let the choice to the user for the model, and also for the number of estimators used.
After that, the program will create the model and predict values based on the user's choices. All models' data are given to Mlflow.
Some metrics are calculated using scikit-learn, in order to see what model and what parameters are the most efficient.
