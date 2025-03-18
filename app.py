import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = 'D:\STUDY\PROJECTS\prediction_models\heart\logistic_regression_heart_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Heart Disease Prediction App")
st.write("Enter the required details to check if you might have a heart problem.")

# Disclaimer
st.warning("This is a machine learning model and is not fully accurate. The predictions should not be considered a substitute for professional medical advice. Please consult a doctor for an accurate diagnosis.")

# Collect user inputs
age = st.number_input("Age", min_value=1, max_value=120, step=1)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type (CP)", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, step=1)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, step=1)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, step=1)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
ca = st.slider("Number of Major Vessels Colored by Fluoroscopy", 0, 4, 0)
thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# Convert inputs to match model requirements
sex = 1 if sex == "Male" else 0
cp = ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"].index(cp)
fbs = 1 if fbs == "Yes" else 0
restecg = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(restecg)
exang = 1 if exang == "Yes" else 0
slope = ["Upsloping", "Flat", "Downsloping"].index(slope)
thal = ["Normal", "Fixed Defect", "Reversible Defect"].index(thal)

# Prepare data for prediction
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease! Please consult a doctor.")
    else:
        st.success("✅ Low risk of heart disease! Maintain a healthy lifestyle.")
