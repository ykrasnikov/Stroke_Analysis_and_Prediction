from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from xgboost import XGBClassifier
from modelHelper import ModelHelper

#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

#endpoint
# Favicon
@app.route('/brain.icon')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'brain.icon',mimetype='image/vnd.microsoft.icon')

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    content = request.json["data"]

    # parse
    sex_label = int(content["sex_label"])
    age = float(content["age"])
    married_label = int(content["married_label"])
    heart_disease = int(content["heart_disease"])
    smoke_hist = int(content["smoke_hist"])
    work_type = int(content["work_type"])
    hypertension = int(content["hypertension"])
    avg_glucose_level = float(content["avg_glucose_level"])
    bmi = float(content["bmi"])
    residence_label = int(content["residence_label"])

    
    # #dummy data
    # sex_label = 1
    # age = 25
    # married_label = 0
    # heart_disease = 0
    # smoke_hist = 3
    # work_type = 3
    # hypertension = 0
    # avg_glucose_level = 200
    # bmi = 40
    # residence_label = 1


    prediction = modelHelper.makePredictions(age, hypertension, heart_disease, avg_glucose_level, bmi, sex_label,  married_label, residence_label, work_type, smoke_hist)
    print(prediction)
    return(jsonify({"ok": True, "prediction": str(prediction)}))

####################################
# ADD MORE ENDPOINTS

###########################################

#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)