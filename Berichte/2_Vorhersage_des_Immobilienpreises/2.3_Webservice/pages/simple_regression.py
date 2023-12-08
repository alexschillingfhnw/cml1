import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from scipy import stats
import os
import locale
import pickle
locale.setlocale(locale.LC_ALL, 'de_CH.UTF-8')


os.chdir(os.path.dirname(os.path.abspath(__file__)))
loaded_model = pickle.load(open('../../../99_gespeicherte_modelle/linreg_model.sav', 'rb'))


def predict(model, X):
    return np.square(model.predict(np.sqrt(X)))
# make title
st.title('Immo-Calculator')

# make input fields
with st.form(key='my_form'):
    living_space = st.number_input(label='SQM Living Space')
    submit_button = st.form_submit_button('Submit')

    if submit_button:
        # make prediction
        X = pd.DataFrame({'Living_area_unified': [living_space]})
        prediction = predict(loaded_model, X)
        prediction_local = locale.format_string('%.2f', prediction[0], True)
        st.subheader(f'Predicted Price: {prediction_local} CHF')
        
