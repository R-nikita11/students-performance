

import pickle
import json
import config
import numpy as np

class StudentsPerformance():

    def __init__(self, Hours_Studied, Previous_Scores, Extracurricular_Activities,
       Sleep_Hours, Sample_Question_Papers_Practiced) :
        self.Hours_Studied =Hours_Studied
        self.Previous_Scores = Previous_Scores
        self.Extracurricular_Activities = Extracurricular_Activities
        self.Sleep_Hours = Sleep_Hours
        self.Sample_Question_Papers_Practiced = Sample_Question_Papers_Practiced
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)

    def get_predicted_performance(self):
        self.load_model()

        # test_array = np.zeros(self.model.n_features_in_)
        test_array = np.zeros(len(self.project_data['columns']))
        
        test_array[0] = self.Hours_Studied
        test_array[1] = self.Previous_Scores
        test_array[2] = self.project_data ['Extracurricular_Activities'][self.Extracurricular_Activities]
        test_array[3] = self.Sleep_Hours
        test_array[4] = self.Sample_Question_Papers_Practiced

        print('Test Array :',test_array)

        predicted_performance= self.model.predict([test_array])[0]
        print(f'students performance: Rs. {round(predicted_performance,2)}')
        

        return predicted_performance


if __name__ == '__main__':
    # Hours_Studied = 7
    # Previous_Scores = 91
    # Extracurricular_Activities = 'Yes'
    # Sleep_Hours = 7
    # Sample_Question_Papers_Practiced = 8
    obj = StudentsPerformance(Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleep_Hours,Sample_Question_Papers_Practiced)

    obj.get_predicted_performance()