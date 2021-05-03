import pandas as pd
import datetime
import time
import pickle
import numpy as np
from xgboost import XGBClassifier

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, age, hypertension, heart_disease, avg_glucose_level, bmi, sex_label,  married_label, residence_label, work_type, smoke_hist):
        work_type_govt_job = 0
        work_type_never_worked = 0
        work_type_private = 0
        work_type_self_employed = 0
        work_type_children = 0

        smoking_status_unknown = 0
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0

        # parse work type
        if (work_type == 1):
            work_type_govt_job = 1
        elif (work_type == 2):
            work_type_never_worked = 1
        elif (work_type == 3):
            work_type_private = 1
        elif (work_type == 4):
            work_type_self_employed = 1
        elif (work_type == 5):
            work_type_children = 1
        else:
            pass

        # parse smoke history
        if (smoke_hist == 1):
            smoking_status_unknown = 1
        elif (smoke_hist == 2):
            smoking_status_formerly_smoked = 1
        elif (smoke_hist == 3):
            smoking_status_never_smoked = 1
        elif (smoke_hist == 4):
            smoking_status_smokes = 1
        else:
            pass
       

        input_pred = [[age, hypertension, heart_disease, avg_glucose_level, bmi, sex_label,  married_label, residence_label, work_type_govt_job, work_type_never_worked, work_type_private, work_type_self_employed, work_type_children, smoking_status_unknown, smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_smokes]]
        pass

        filename = 'finalized_model.sav'
        ada_load = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = ada_load.predict_proba(X)
        preds_singular = ada_load.predict_proba(X)[:,1]

        return preds_singular[0]