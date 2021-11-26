import shap
import numpy as np

def modelshap(model, X_test, predictions):
	explainer = shap.TreeExplainer(model)
	shap_values = explainer.shap_values(X_test)
    np.abs(shap_values.sum(1) + explainer.expected_value - predictions).max()
    shap.summary_plot(shap_values, X_test)
    return 0