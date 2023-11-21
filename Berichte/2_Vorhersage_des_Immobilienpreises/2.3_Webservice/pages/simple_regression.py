import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from scipy import stats
import os
import locale
locale.setlocale(locale.LC_ALL, 'de_CH.UTF-8')


os.chdir(os.path.dirname(os.path.abspath(__file__)))

def fit_linear_regression(X, y, transformation_func=None):
    # Apply transformation if provided
    if transformation_func:
        X = transformation_func(X)
    
    # Train linear regression model
    lin_reg = LinearRegression()
    if len(X.shape) == 1:
        lin_reg.fit(X.values.reshape(-1, 1), y)
    else:
        lin_reg.fit(X, y)
    return lin_reg

def predict(model, X):
    if len(X.shape) == 1:
        return model.predict(X.values.reshape(-1, 1))
    else:
        return model.predict(X)


df = pd.read_csv('../../../../data/immo_data_clean.csv', low_memory=False)
df = df[['Living_area_unified', 'Floor space','price_cleaned']]
df = df.dropna(subset=['Living_area_unified','Floor space'], how='all')
df['Living_area_unified'] = df['Living_area_unified'].fillna(df['Floor space'])
z = np.abs(stats.zscore(df['Living_area_unified']))
df_temp = df[(z < 18)]
X34 = df['Living_area_unified']
y34 = df['price_cleaned']
model = fit_linear_regression(X34, y34, None)

# make title
st.title('Immo-Calculator')

# make input fields
with st.form(key='my_form'):
    living_space = st.number_input(label='SQM Living Space')
    submit_button = st.form_submit_button('Submit')

    if submit_button:
        # make prediction
        X = pd.DataFrame({'Living_area_unified': [living_space]})
        prediction = predict(model, X)
        prediction_local = locale.format_string('%.2f', prediction[0], True)
        st.subheader(f'Predicted Price: {prediction_local} CHF')
        
