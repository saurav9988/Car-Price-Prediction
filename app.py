from flask import Flask, render_template, request
import pickle
import jsonify
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import requests

app = Flask(__name__)

model=pickle.load(open('random_forest_regression_model.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to=StandardScaler()
@app.route('/predict', methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':

        age_of_car = int(request.form['age_of_car'])
        Present_Price = float(request.form['present_price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol == "Petrol"):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0
        elif(Fuel_Type_Petrol == 'Diesel'):
            Fuel_Type_Diesel=1
            Fuel_Type_Petrol=0
        else:
            Fuel_Type_Diesel=0
            Fuel_Type_Petrol=0

        age_of_car =2020-age_of_car
        
        Seller_Type_Individual = request.form['Seller_Type_Individual']
        if (Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0

        Transmission_Manual = request.form['Transmission_Manual']
        if(Transmission_Manual=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        prediction=model.predict([[Present_Price, Kms_Driven, Owner, age_of_car,Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual,Transmission_Manual]])
        output=prediction[0]

        return render_template('result.html', prediction_result=output)

if __name__ == '__main__':
    app.run(debug=True)
