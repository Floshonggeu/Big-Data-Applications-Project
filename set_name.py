# from project import chosenmodel
# import project

def namemodel(chosenmodel):
    if (chosenmodel == 1):
        modelname = 'Random Forest'
    elif (chosenmodel == 2):
        modelname = 'Gradient Boosting'
    else:
        modelname = 'XGBoost'
    return modelname