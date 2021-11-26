from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np

def eval_metrics(Y_test, predictions):
    # Calculating mean squared error
    msqe = np.sqrt(mean_squared_error(Y_test, predictions))
    # Calculating mean absolute error
    mae = mean_absolute_error(Y_test, predictions)
    # Calculating coefficient of determination (R²)
    r2 = r2_score(Y_test, predictions)
    # Calculating global accuracy using scikit-learn
    accuracy = metrics.accuracy_score(Y_test, predictions)
    return msqe, mae, r2, accuracy