

import streamlit as st
import pandas as pd
import numpy as np
import pickle


loaded_model = pickle.load(open('advertising.sav', 'rb'))


st.title("Sales Prediction")
TV = st.number_input("Enter amount for TV Channel:")
radio = st.number_input("Enter amount for Radio Channel:")


if(st.button("Predict")):
	ypred = loaded_model.predict([[TV, radio]])
	st.write(f"Predicted Sales Amount (in Millions):{ypred[0]}")





