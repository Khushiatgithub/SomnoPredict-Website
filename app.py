from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__, static_folder="static")

# Load trained model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Encoders for categorical variables
gender_map = {"Male":0, "Female":1}
occupation_map = {
    "Doctor":0, "Engineer":1, "Teacher":2, "Nurse":3, "Lawyer":4,
    "Sales":5, "Manager":6, "Scientist":7, "Student":8, "Accountant":9
}
bmi_map = {"Underweight":0, "Normal":1, "Overweight":2, "Obese":3}
disorder_map = {"None":0, "Insomnia":1, "Sleep Apnea":2, "Restless Leg Syndrome":3}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get form values
        gender = gender_map[request.form["gender"]]
        age = int(request.form["age"])
        occupation = occupation_map[request.form["occupation"]]
        sleep = float(request.form["sleep"])
        activity = float(request.form["activity"])
        stress = float(request.form["stress"])
        bmi = bmi_map[request.form["bmi"]]
        heart = float(request.form["heart"])
        steps = float(request.form["steps"])
        disorder = disorder_map[request.form["disorder"]]

        bp = request.form["bp"].split("/")
        systolic = int(bp[0])
        diastolic = int(bp[1])

        # Ensure feature order matches training
        features = np.array([[gender, age, occupation, sleep, activity, stress,
                              bmi, heart, steps, systolic, diastolic, disorder]])

        # Scale features
        features_scaled = scaler.transform(features)

        # Make prediction
        prediction = model.predict(features_scaled)[0]

        return render_template("index.html", result=round(prediction,2))

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
