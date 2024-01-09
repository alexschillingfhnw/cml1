import pandas as pd
import numpy as np
import streamlit as st
import os
import locale
import pickle

# set locale to german (Switzerland)
locale.setlocale(locale.LC_ALL, 'de_CH.UTF-8')

# change working directory so we can work with relative paths
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# load model
loaded_model = pickle.load(open('../../../99_gespeicherte_modelle/linreg_model.sav', 'rb'))

#small function to predict price
def predict(model, X):
    return np.square(model.predict(np.sqrt(X)))

# Title
st.title('Immo-Calculator')
# Instructions
st.text("Enter Living Space of your Property in sqm")
# Simple form
with st.form(key='my_form'):
    # Input
    living_space = st.number_input(label='SQM Living Space')
    # Submit Button
    submit_button = st.form_submit_button('Submit')
    # Prediction
    if submit_button:
        X = pd.DataFrame({'Living_area_unified': [living_space]})
        prediction = predict(loaded_model, X)
        # Format prediction to CHF
        prediction_local = locale.format_string('%.2f', prediction[0], True)
        # Print prediction
        st.subheader(f'Predicted Price: {prediction_local} CHF')
        
