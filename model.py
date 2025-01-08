import sys
sys.path.append("/opt/anaconda3/lib/python3.9/site-packages")
import streamlit as st
import joblib
import pandas as pd
import numpy as np
# Title of the app
#st.write("# Welcome to Chinese Stock Market Price Prediction")

# Title of the app with two lines using markdown
st.markdown("<h1 style='text-align: center;'>Welcome to Chinese Stock</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Market Price Prediction</h1>", unsafe_allow_html=True)

# Create three columns for user input
col1, col2, col3 = st.columns(3)

# Input fields for user to enter stock data
openP = col1.number_input("Enter your Stock's Open Price", min_value=0.0)
highP = col2.number_input("Enter your Stock's High Price", min_value=0.0)
lowP = col3.number_input("Enter your Stock's Low Price", min_value=0.0)
volumeP = col1.number_input("Enter your Stock's Volume", min_value=0)
ema50 = col2.number_input("Enter your Stock's EMA-50", min_value=0.0)
ema200 = col3.number_input("Enter your Stock's EMA-200", min_value=0.0)

# Load the trained model 
model = joblib.load('lr_model.pkl')  # Adjust the path to where your model is stored

# Define a function to predict stock price using the user inputs
def predict_stock_price(openP, highP, lowP, volumeP, ema50, ema200):
    # Convert inputs to a numpy array (model expects an array)
    input_data = np.array([[openP, highP, lowP, volumeP, ema50, ema200]])
    
    # Make prediction using the loaded model
    prediction = model.predict(input_data)
    return prediction[0]

# Button to trigger prediction
if st.button('Predict'):
    if openP and highP and lowP and volumeP and ema50 and ema200:
        # Make prediction using the user input
        prediction = predict_stock_price(openP, highP, lowP, volumeP, ema50, ema200)
        
        # Display the prediction result
        st.write(f"The predicted stock price is: {prediction}")
    else:
        st.write("Please enter all the values before predicting.")

        # type below on the terminal
        # streamlit run model.py