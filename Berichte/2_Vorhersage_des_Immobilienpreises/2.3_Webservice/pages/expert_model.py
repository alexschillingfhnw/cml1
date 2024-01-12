import pandas as pd
import numpy as np
import streamlit as st
import os
import locale
import pickle

# change working directory so we can work with relative paths
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# loading Model and Scaled created in 2.2 Model Training
loaded_model = pickle.load(open('../../../99_gespeicherte_modelle/hgb_regression_log.sav', 'rb'))
scaler = pickle.load(open('../../../99_gespeicherte_modelle/scaler.pkl', 'rb'))

# simple function to predict price
def predict(model, X):
    return model.predict(X)

# Page Title
st.title('Immo-Calculator')

# Form to enter user inputs
with st.form(key='my_form'):
    # Column Names, allows semi-automated creation of form - also helps when model features change
    column_names = ['Year built:', 'Living_area_unified',
       'Plot_area_unified', 'Rooms_new', 'gde_workers_total',
       'gde_area_agriculture_percentage', 'gde_area_forest_percentage',
       'gde_area_nonproductive_percentage', 'gde_area_settlement_percentage',
       'gde_average_house_hold', 'gde_empty_apartments',
       'gde_foreigners_percentage', 'gde_new_homes_per_1000',
       'gde_pop_per_km2', 'gde_population', 'gde_private_apartments',
       'gde_social_help_quota', 'gde_tax', 'kanton_AI', 'kanton_AR',
       'kanton_BE', 'kanton_BL', 'kanton_BS', 'kanton_FR', 'kanton_GE',
       'kanton_GL', 'kanton_GR', 'kanton_JU', 'kanton_LU', 'kanton_NE',
       'kanton_NW', 'kanton_OW', 'kanton_SG', 'kanton_SH', 'kanton_SO',
       'kanton_SZ', 'kanton_TG', 'kanton_TI', 'kanton_UR', 'kanton_VD',
       'kanton_VS', 'kanton_ZG', 'kanton_ZH']

    # Lists for Selectboxes
    kanton_list = [col.split("_")[-1] for col in column_names if col.startswith("kanton_")]
    #type_unified_list = [col.split("_")[-1] for col in column_names if col.startswith("type_unified_")]
    user_inputs = {}
    # Create Form, starting with title
    st.title("Expert Form")

    # Every non categorical feature gets a number input, others are skipped here
    for column_name in column_names:
        if column_name.startswith("kanton_") or column_name.startswith("type_") or column_name.startswith("Availability_"):
            pass
        else:
            user_inputs[column_name] = st.number_input(f"Enter {column_name}")
    # Selectboxes for categorical features
    kanton = st.selectbox(f"Select Canton", kanton_list)
    #type_unified = st.selectbox(f"Select Type") #, type_unified_list)
    
    # Submit Button
    submit_button = st.form_submit_button('Submit')

    # Submit button handling
    if submit_button:
        # Delete old result_df if it exists to avoid errors when user changes input
        if 'result_df' in locals():
            del result_df
        # Creates dummy dataframes for categorical features
        df_kanton = pd.DataFrame({col: [1] if col == f"kanton_{kanton}" else [0] for col in column_names if col.startswith("kanton_")})
        #df_type_unified = pd.DataFrame({col: [1] if col == f"type_unified_{type_unified}" else [0] for col in column_names if col.startswith("type_unified_")})
        # Creates dataframe from user inputs
        df_user_inputs = pd.DataFrame([user_inputs])
        # Replaces 0 with NaN to avoid errors when scaling
        df = pd.DataFrame([user_inputs])
        df = df.replace(0.0, np.nan)
        # Concatenates all dataframes
        result_df = pd.concat([df, df_kanton], axis=1)#, df_type_unified], axis=1)
        # Scales dataframe
        result_df_standardized = pd.DataFrame(scaler.transform(result_df), columns=result_df.columns)
        # Predicts price
        prediction = 0
        prediction = predict(loaded_model, result_df_standardized)
        prediction = np.exp(prediction)
        # changes locale to CHF and formats prediction
        locale.setlocale(locale.LC_ALL, 'de_CH.UTF-8')
        prediction_local = locale.format_string('%.2f', prediction[0], True)
        # Prints prediction and dataframe
        st.write(f'Predicted Price: {prediction_local} CHF')
        st.write(result_df)

# Alternative Input Option - List
st.title("List Input Option")
# Text Area for user input
list_input = st.text_area(" Alternative: Enter a list of values separated by semicolons (Kanton and Type already as dummies):", "")
# separate values by semicolon
list_values = [float(val) for val in list_input.split(";") if val.strip()]

# Button to predict from list
if st.button("Predict from List"):
    # small error handling
    if not list_values:
        st.warning("Please enter a valid list of values.")
    else:
        # Delete old result_df if it exists to avoid errors when user changes input
        if 'result_df' in locals():
            del result_df
        # make dic from column names and list values and create dataframe
        user_inputs_list = dict(zip(column_names, list_values))
        df = pd.DataFrame([user_inputs_list])
        # replace 0 with NaN to avoid errors when scaling
        result_df = df.replace(0.0, np.nan)
        # scale dataframe
        result_df_standardized = pd.DataFrame(scaler.transform(result_df), columns=result_df.columns)
        # predict price
        prediction = predict(loaded_model, result_df_standardized)
        prediction = np.exp(prediction)
        # change locale to CHF
        prediction_local = locale.format_string('%.2f', prediction[0], True)
        st.write(f'Predicted Price from List: {prediction_local} CHF')
        st.write(result_df)
        
