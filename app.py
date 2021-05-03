from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from xgboost import XGBClassifier
from modelHelper import ModelHelper
import logging

#init app and class
app = Flask(__name__,static_url_path='/static')
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 - Tried changing to 1
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
modelHelper = ModelHelper()

#endpoint
# Favicon    
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# @app.route("/nav")
# def nav():
#     # Return template and data
#     return render_template("navbar_template.html")

# @app.route("/head")
# def head():
#     # Return template and data
#     return render_template("head_template.html")


# @app.route("/ml")
# def model_page():
#     # Return template and data
#     return render_template("ml.html")

# @app.route("/vizz_mortality")
# def dashboard1():
#     # Return template and data
#     return render_template("MortalityRateVizz.html")

# @app.route("/vizz_risk")
# def dashboard2():
#     # Return template and data
#     return render_template("StrokeRiskVizz.html")

# @app.route("/vizz_explore")
# def dashboard3():
#     # Return template and data
#     return render_template("DataExploreVIZZ.html")

# @app.route("/data_display")
# def data():
#     # Return template and data
#     return render_template("Data.html")

# @app.route("/exploration")
# def exploration():
#     # Return template and data
#     return render_template("exploration.html")

# @app.route("/resources")
# def resources():
#     # Return template and data
#     return render_template("resources.html")

# @app.route("/team")
# def about_us():
#     # Return template and data
#     return render_template("team.html")

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
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)