import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app

flask_app = Flask(__name__)

# Load model
model = pickle.load(open("newest_model.pkl", "rb"))

@flask_app.route("/")

def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    
    if prediction == [1]:
        prediction_value =  "Malignant"
    else:
        prediction_value = "Benign"

    return render_template("index.html", prediction_text = "The cell is {}".format(prediction_value))

if __name__ == "__main__":
    flask_app.run(debug = True)