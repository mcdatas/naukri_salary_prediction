from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)
# load the pickel model
model = pickle.load(open("model1.pkl", "rb"))

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/predict',methods=['POST','GET'])
def predict():

    features = [int(x) for x in request.form.values()]  
    if sum(features) == 0:
        output = 0
        return render_template('index.html', prediction_text='Annual Avg Salary should be Rs. {}'.format(output))
    else:
        final_features = np.array([features])
        prediction = model.predict(final_features)
 
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text='Annual Avg Salary should be Rs. {}'.format(output))



if __name__ == '__main__':
    
     app.run(debug = True)
