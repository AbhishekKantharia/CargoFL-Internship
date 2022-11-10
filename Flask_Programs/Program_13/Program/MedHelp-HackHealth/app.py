#importing the required libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#creation of the Flask Application named as "app"
app = Flask(__name__)

#loading the pickle files of all 3 models which are used in read binary mode
model1 = pickle.load(open('diabetesmodel.pkl', 'rb'))
model2 = pickle.load(open('covid19model.pkl', 'rb'))
model3 = pickle.load(open('heartdiseasemodel.pkl', 'rb'))

#home page - routing to the home page is done
@app.route('/home')
@app.route('/')
def home():
    #renders the home page template 
    return render_template('home.html')

#diabetets page - routing to diabetes prediction page
@app.route('/d')
def d():
    #renders the diabetes prediction page template
    return render_template('diabetesindex.html')

#covid19 page - routing to covid19 prediction page
@app.route('/c')
def c():
    #renders the covid19 prediction page template
    return render_template('covid19index.html')

#heart disease page - routing to heart disease prediction page
@app.route('/h')
def h():
    #renders the heart disease prediction page template
    return render_template('heartdiseaseindex.html')

#medical suggestions page - routing to medical suggestions page
@app.route('/m')
def m():
    #renders the medicaL suggestions page template
    return render_template('medicalsuggestions.html')

#portion for diabetes prediction
@app.route('/di',methods=['POST'])
def diabetespredict():
    #4 features - Glucose, Insulin, Body Mass Index, Age
    int_features = [int(x) for x in request.form.values()]
    #convert the features to numpy array
    final_features = [np.array(int_features)]
    #predict the output on basis of the 4 features fed to the model
    prediction = model1.predict(final_features)
    #on basis of prediction displaying the desired output
    if prediction=='No':
        data="Not Affected By Diabetes"
    elif prediction=="Yes":
        data="Affected By Diabetes"
    return render_template('diabetesindex.html', prediction_text1='Health Status: {}'.format(data))

#portion for covid-19 prediction
@app.route('/ci',methods=['POST'])
def covid19predict():
    #4 featues - Dry Cough, Fever, Sore Throat, Breathing Problem
    int_features = [int(x) for x in request.form.values()]
    #convert the features to numpy array
    final_features = [np.array(int_features)]
    #predict the output on basis of the 4 features fed to the model
    prediction = model2.predict(final_features)
    #on basis of prediction displaying the desired output
    if prediction==0:
        data="Not Affected By Covid-19"
    elif prediction==1:
        data="Affected By Covid-19"
    return render_template('covid19index.html', prediction_text2='Health Status: {}'.format(data))

#portion for heart disease prediction
@app.route('/hi',methods=['POST'])
def heartdiseasepredict():
    #4 features - Chest Pain, Blood Pressure, Cholestrol, Max Heart Rate
    int_features = [int(x) for x in request.form.values()]
    #convert the features to numpy array
    final_features = [np.array(int_features)]
    #predict the output on basis of the 4 features fed to the model
    prediction = model3.predict(final_features)
    #on basis of prediction displaying the desired output
    if prediction=="Absence":
        data="Not Affected By Heart Disease"
    elif prediction=="Presence":
        data="Affected By Heart Disease"
    return render_template('heartdiseaseindex.html', prediction_text3='Health Status: {}'.format(data))

#debug is set to True in development environment and set to False in production environment
if __name__ == "__main__":
    app.run(debug=True)
