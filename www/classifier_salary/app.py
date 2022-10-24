from flask import Flask,request
from flask_restful import Resource, Api
from flask_restful import reqparse
import pickle
import numpy as np
import pandas as pd
from flask_cors import CORS
import joblib


app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):   
    def get(self, gender_input, age_input, salary_input):
        #budget = request.args.get('budget')
        print(gender_input)
        age_input = int(age_input)
        salary_input = float(salary_input)
        if(gender_input == 'Male'):
            gender_input = 1
        else:
            gender_input = 0
        # Let's load the package
        df = pd.DataFrame({"Gender":[gender_input], "Age":[age_input], "EstimatedSalary_K":[salary_input]})
        model = joblib.load("lr_model.pkl")
        prediction = model.predict(df)
        if(prediction == 0):
            return 'NO'
        else:
            return 'YES'
        #prediction = int(prediction[0])
        #return str(prediction)

#
api.add_resource(prediction, '/prediction/<string:gender_input>/<string:age_input>/<string:salary_input>')

if __name__ == '__main__':
    app.run(debug=True)