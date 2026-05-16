import streamlit as st
import pandas as pd
import numpy as np
import pickle


loaded_model = pickle.load(open('advertising.sav', 'rb'))

st.title("Sales Prediction Application")
TV = st.number_input("Enter amount for TV Channels:")
radio = st.number_input("Enter amount for Radio Channels:")

if(st.button("Predict Sales")):
    ypred = loaded_model.predict([[TV, radio]])
    st.write(f"The Predicted Sales would be : {ypred[0]}")
