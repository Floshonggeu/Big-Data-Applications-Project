import pandas as pd
from sklearn.model_selection import train_test_split

def cut_xy(featured_data):
    # Setting target as the predicted variable
    Y = featured_data["TARGET"]
    # Dropping target from the original dataset
    X = featured_data.drop(columns = ['TARGET'])
    return X, Y

def traintestsplit(X, Y):
    # Using scikit-learn to split into train and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    return X_train, X_test, Y_train, Y_test