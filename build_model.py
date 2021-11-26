from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.ensemble import GradientBoostingClassifier

def initializemodel(chosenmodel, estimators):
    if (chosenmodel == 1):
        # Initialize Random Forest Classifier model
        model = RandomForestClassifier(n_estimators = estimators)
    elif (chosenmodel == 2):
        # Initialize Gradient Boosting model
        model = GradientBoostingClassifier(n_estimators = estimators)
    elif (chosenmodel == 3):
        # Initialize XGBoost model
        model = xgb.XGBClassifier(n_estimators = estimators, use_label_encoder = False)
    return model