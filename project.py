# Importing libraries
import pandas as pd
import mlflow
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier

#Importing others .py files
import feature_eng
import split
import choose_from_user
import build_model
import calculate_accuracy
import set_name
import shapper

# Read data from csv file
raw_data = pd.read_csv("application_train.csv")

# Doing some feature engineering
featured_data = feature_eng.featureengineering(raw_data)

# Separating Target from original dataset
X, Y = split.cut_xy(featured_data)

# Splitting data into train and test sets
X_train, X_test, Y_train, Y_test = split.traintestsplit(X, Y)

# Initializing variable to build multiple models
another = 1

while (another == 1):

	# Asking user what model he wants to use
	chosenmodel = choose_from_user.choiceloop()

	# Asking user how many estimators he wants to use
	estimators = choose_from_user.chooseestimators()

	# Building models
	with mlflow.start_run():
	    # Initializing the model with user's choices
	    model = build_model.initializemodel(chosenmodel, estimators)
	    
	    # Fitting the model
	    model.fit(X_train, Y_train)
	    
	    # Predicting targets
	    predictions = model.predict(X_test)
	    
	    # Calculating accuracy parameters
	    msqe, mae, r2, accuracy = calculate_accuracy.eval_metrics(Y_test, predictions)
	    
	    # Defining chosen model name
	    chosenmodelname = set_name.namemodel(chosenmodel)
	    
	    # Logging parameters to MLflow
	    mlflow.log_param("modelname", chosenmodelname)
	    mlflow.log_param("estimators", estimators)
	    
	    # Logging metrics to MLflow
	    mlflow.log_metric("msqe", msqe)
	    mlflow.log_metric("mae", mae)
	    mlflow.log_metric("r2", r2)
	    mlflow.log_metric("accuracy", accuracy)
	    
	    # Logging model to MLflow
	    mlflow.sklearn.log_model(model, "model")

	    # Using shap
	    modelshap(model, X_test, predictions)

	    # Asking user if he wants to build another model
	    another = choose_from_user.anothermodel()