import pandas as pd
#from project import raw_data
#import project

def featureengineering(raw_data):
    # Dropping rows with at least one missing value
    dropped_data = raw_data.dropna(axis = 0)
    # Transforming variables into dummies
    dummied_data = pd.get_dummies(dropped_data, columns = ['NAME_CONTRACT_TYPE', 'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'NAME_TYPE_SUITE', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'OCCUPATION_TYPE', 'WEEKDAY_APPR_PROCESS_START', 'ORGANIZATION_TYPE', 'FONDKAPREMONT_MODE', 'HOUSETYPE_MODE', 'WALLSMATERIAL_MODE', 'EMERGENCYSTATE_MODE'])
    return dummied_data