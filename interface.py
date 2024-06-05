from flask import Flask, jsonify, request, render_template
import config
from utils import StudentsPerformance
import pandas as Pd
import numpy as np


app = Flask(__name__)


@app.route('/')
def performance_model():
    print('Welcome to the Students Performance Model')
    return render_template('index.html')


@app.route('/predict_performance', methods = ['POST'])
def get_students_performance():
        # request.method == 'POST'
        print('We are in POST Method')
        data = request.form
        Hours_Studied = eval(data['Hours_Studied'])
        Previous_Scores = eval(data['Previous_Scores'])
        Extracurricular_Activities = data['Extracurricular_Activities']
        Sleep_Hours =  eval(data['Sleep_Hours'])
        Sample_Question_Papers_Practiced = eval(data['Sample_Question_Papers_Practiced'])
       
        # print(f'Age=={age}, Sex=={sex}, BMI=={bmi}, Children=={children}, Smoker=={smoker}, Region=={region}')

        student_pr = StudentsPerformance(Hours_Studied, Previous_Scores, Extracurricular_Activities,
        Sleep_Hours, Sample_Question_Papers_Practiced)
        prediction = student_pr.get_predicted_performance()
        # return jsonify({ f'students performance: Rs. {round(prediction,2)}'})
        return jsonify({ 'students_performance': f'Rs. {round(prediction, 2)}' })

    
        print(data)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=False)