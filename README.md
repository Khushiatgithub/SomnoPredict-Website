# 🌙 SomnoPredict - AI Sleep Prediction Web App

## Overview
**SomnoPredict** is a machine learning web application that predicts optimal sleep duration based on your lifestyle and health metrics. By analyzing factors like **age, gender, BMI, blood pressure, sleep disorders, and occupation**, etc the app provides personalized sleep insights to help improve overall sleep quality.  

---

<img width="1816" height="872" alt="Screenshot 2026-08-24 183910" src="https://github.com/user-attachments/assets/5462f58f-ac18-4f1c-86ea-5e7de60622eb" />



## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **Deployment:** Render  

---

## Dataset
- **Source:** Sleep Health and Lifestyle Dataset  
- **Records:** 374  
- **Features:** Age, Gender, Occupation, BMI Category, Blood Pressure, Sleep Duration, Sleep Disorders  

---

## Web App Features
- Responsive intake form for collecting user data  
- Predicts personalized sleep duration  
- User-friendly interface with CSS styling  
- Handles multiple input types (dropdowns, text, numeric inputs)  

---

## How to Run Locally
1. Clone the repository:  
```bash
git clone https://github.com/YourUsername/SomnoPredict-Website.git
Navigate to the project folder:

cd SomnoPredict-Website
Install dependencies:

pip install -r requirements.txt
Run the Flask app:

python app.py
Open your browser at http://127.0.0.1:5000

Deployment
Can be deployed on Render, Heroku, or similar platforms

Use gunicorn app:app as the start command for production deployment

Future Scope
Add lifestyle and sleep recommendations

Integrate real-time sleep tracking from wearable devices

Provide analytics dashboards for user sleep patterns

Project Structure
SomnoPredict-Website/
│
├── app.py                # Flask application
├── model.pkl             # Trained Random Forest model
├── scaler.pkl            # StandardScaler object
├── requirements.txt      # Python dependencies
├── runtime.txt           # Python version for deployment
├── templates/
│   └── index.html        # HTML template
└── static/
    └── style.css         # CSS styling



