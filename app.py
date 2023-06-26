import streamlit as st
from utils import preprocess_input, columns

import pandas as pd
import numpy as np
import joblib

model = joblib.load('rfc_model.joblib')

st.title('Does your machine need maintenance? 🔨👷‍♀️👨‍🏭🏢')
machine_type = st.selectbox('Input Machine Type', ['L - Lower Grade', 'M - Medium Grade', 'H - High Grade'])
air_temp = st.slider('Choose Air temperature [K]', 295,310)
proc_temp = st.slider('Choose Process temperature [K]', 300,320)
rpm = st.slider('Choose Rotational speed [rpm]', 1150,2890)
torq = st.slider('Choose Torque [Nm]', 2,80)
tool_wear = st.slider('Choose Tool wear [min]', 10,260)
power = torq * rpm

def predict():
    row = np.array([machine_type, air_temp, proc_temp,
                    rpm, torq, tool_wear, power])
    X = pd.DataFrame([row], columns=columns)
    processed_df = preprocess_input(X)
    prediction = model.predict(processed_df)[0]

    if prediction == 1:
        st.error('Machine in need of maintainence 🔨🧰')
    else:
        st.success('Everything is alright with your machine 🐱‍🏍')

st.button('Predict', on_click=predict)
