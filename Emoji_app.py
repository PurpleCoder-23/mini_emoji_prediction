# app.py
import streamlit as st
import joblib
import numpy as np
import os


# Load the trained model

path = os.path.join("C:\\", "Users", "HOME", "Downloads", "emoji_model.joblib")
print(f"Loading model from: {path}")
model = joblib.load(path)



st.title("Emoji Predictor 😊📊")

# User input
age = st.number_input("Enter your age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Select your gender", ["male", "female"])

# Map gender to number
gender_encoded = 0 if gender == "male" else 1

# Prediction
if st.button("Predict Emoji"):
    features = np.array([[age, gender_encoded]])
    prediction = model.predict(features)
    st.success(f"Predicted Emoji: {prediction[0]}")
