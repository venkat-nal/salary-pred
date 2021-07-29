from flask import Flask, render_template, redirect, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("hiring.pkl",'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Employee Salary should be $ {output}')


if __name__ == "__main__":
    app.run(debug=True)