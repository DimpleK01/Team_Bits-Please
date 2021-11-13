from flask import Flask, render_template, request
from sklearn.linear_model import LogisticRegression
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/home.html")
def home2():
    return render_template('home.html')

@app.route("/webpage.html")
def diabetes():
    return render_template('webpage.html')

@app.route("/heart_webpage.html")
def heart():
    return render_template('heart_webpage.html')

@app.route("/result",methods=["GET", "POST"])
def diabetes_result():
    result=""
    pregnancies = int(float(request.form['pregnancies']))
    Glucose = int(float(request.form['Present_Price']))
    blood_pressure = int(float(request.form['BloodPressure']))
    skin_thickness = int(float(request.form['SkinThickness']))
    Insulin = int(float(request.form['Insulin']))
    BMI = int(float(request.form['BMI']))
    Diabetes_Pedigree_Function = int(float(request.form['DiabetesPedigreeFunction']))
    Age = int(float(request.form['Age']))
    data = pd.read_csv('C:/Users/dimp1/Desktop/Disease_prediction_Project/untitled5/diabetes.csv')
    x = data[['Pregnancies', 'Glucose', 'blood pressure', 'skin thickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
    y = data[['Outcome']]
    print(pregnancies, Glucose, blood_pressure, skin_thickness, Insulin, BMI, Diabetes_Pedigree_Function, Age)
    logreg = LogisticRegression(solver='lbfgs', max_iter=1000)
    logreg.fit(x, y)
    #y_pred = logreg.predict([[Pregnancies, Glucose, blood_pressure, skin_thickness, Insulin, BMI, Diabetes_Pedigree_Function, Age]])
    y_pred = logreg.predict([[8, 176, 90, 34, 300, 33.7, 0.467, 58]])
    print(y_pred[0])
    if y_pred[0] == 1:
        print("Diabetic")
        result="You are at a risk for diabetes!!! Please consult a doctor immediately"
    else:
        print("Not Diabetic")
        result="You are not at a risk for diabetes"
    return render_template("result.html",result=result)

@app.route("/heart_result",methods=["GET", "POST"])
def heart_result():
    result=""
    age = int(float(request.form['Age']))
    anemia = int(float(request.form['Anemia']))
    creatinine_phosphokinase = int(float(request.form['creatinine_phosphokinase']))
    Diabetes = int(float(request.form['Diabetes']))
    ejection_fraction = int(float(request.form['ejection_fraction']))
    hbp = int(float(request.form['HBP']))
    Platelets = int(float(request.form['Platelets']))
    serum_creatinine = int(float(request.form['serum_creatinine']))
    serum_sodium = int(float(request.form['serum_sodium']))
    gender = int(float(request.form['gender']))
    data = pd.read_csv('C:/Users/dimp1/Desktop/Disease_prediction_Project/untitled5/heart_failure_prediction.csv')
    x = data[['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'platelets', 'serum_creatinine', 'serum_sodium', 'gender']]
    y = data[['DEATH_EVENT']]
    print(age, anemia, creatinine_phosphokinase, Diabetes, ejection_fraction, hbp, Platelets, serum_creatinine,serum_sodium,gender)
    logreg = LogisticRegression(solver='lbfgs', max_iter=1000)
    logreg.fit(x, y)
    #y_pred = logreg.predict([[Pregnancies, Glucose, blood_pressure, skin_thickness, Insulin, BMI, Diabetes_Pedigree_Function, Age]])
    y_pred = logreg.predict([[50,1,111,0,20,0,210000,1.9,137,1]])
    print(y_pred[0])
    if y_pred[0] == 1:
        print("Risk at Heart Failure")
        result="You are at a risk for heart failure!!! Please consult a doctor immediately."
    else:
        print("Normal")
        result="You are not at a risk for heart failure."
    return render_template("result.html",result=result)


app.run()
