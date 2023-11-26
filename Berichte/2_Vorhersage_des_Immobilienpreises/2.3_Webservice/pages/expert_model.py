import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from scipy import stats
import os
import locale
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_percentage_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.impute import KNNImputer
import pickle
os.chdir(os.path.dirname(os.path.abspath(__file__)))

loaded_model = pickle.load(open('../../../99_gespeicherte_modelle/xgboost_model_big.sav', 'rb'))


def predict(model, X):
    return model.predict(X)


st.title('Immo-Calculator')


with st.form(key='my_form'):
    column_names = ["Zip", "Year built:", "Living_area_unified", "Floor_unified", "Floor_space_merged", 
                    "Plot_area_unified", "Rooms_new", "gde_workers_sector1", "gde_workers_sector2", 
                    "gde_workers_sector3", "gde_workers_total", "distanceToTrainStation", 
                    "gde_area_agriculture_percentage", "gde_area_forest_percentage", 
                    "gde_area_nonproductive_percentage", "gde_area_settlement_percentage", 
                    "gde_average_house_hold", "gde_empty_apartments", "gde_foreigners_percentage", 
                    "gde_new_homes_per_1000", "gde_pop_per_km2", "gde_population", 
                    "gde_private_apartments", "gde_social_help_quota", "gde_tax", "gde_politics_bdp", 
                    "gde_politics_cvp", "gde_politics_evp", "gde_politics_fdp", "gde_politics_glp", 
                    "gde_politics_gps", "gde_politics_pda", "gde_politics_rights", "gde_politics_sp", 
                    "gde_politics_svp", "NoisePollutionRailwayL", "NoisePollutionRailwayM", 
                    "NoisePollutionRailwayS", "NoisePollutionRoadL", "NoisePollutionRoadM", 
                    "NoisePollutionRoadS", "PopulationDensityL", "PopulationDensityM", 
                    "PopulationDensityS", "RiversAndLakesL", "RiversAndLakesM", "RiversAndLakesS", 
                    "WorkplaceDensityL", "WorkplaceDensityM", "WorkplaceDensityS", "ForestDensityL", 
                    "ForestDensityM", "ForestDensityS", "kanton_AI", "kanton_AR", "kanton_BE", 
                    "kanton_BL", "kanton_BS", "kanton_FR", "kanton_GE", "kanton_GL", "kanton_GR", 
                    "kanton_JU", "kanton_LU", "kanton_NE", "kanton_NW", "kanton_OW", "kanton_SG", 
                    "kanton_SH", "kanton_SO", "kanton_SZ", "kanton_TG", "kanton_TI", "kanton_UR", 
                    "kanton_VD", "kanton_VS", "kanton_ZG", "kanton_ZH", "type_unified_attic-room", 
                    "type_unified_castle", "type_unified_chalet", "type_unified_detached-house", 
                    "type_unified_detached-secondary-suite", "type_unified_duplex-maisonette", 
                    "type_unified_farmhouse", "type_unified_flat", "type_unified_furnished-residential-property", 
                    "type_unified_loft", "type_unified_penthouse", "type_unified_rustico", 
                    "type_unified_secondary-suite", "type_unified_semi-detached-house", 
                    "type_unified_single-room", "type_unified_stepped-apartment", 
                    "type_unified_stepped-house", "type_unified_studio", "type_unified_terrace-house", 
                    "type_unified_villa", "Availability_Categorized_More than 6 months", 
                    "Availability_Categorized_On request", "Availability_Categorized_Within 1 month", 
                    "Availability_Categorized_Within 3 months", "Availability_Categorized_Within 6 months"]

    availability_list = [col.split("_")[-1] for col in column_names if col.startswith("Availability_Categorized_")]
    kanton_list = [col.split("_")[-1] for col in column_names if col.startswith("kanton_")]
    type_unified_list = [col.split("_")[-1] for col in column_names if col.startswith("type_unified_")]
    user_inputs = {}

    st.title("Expert Form")
    for column_name in column_names:
        if column_name.startswith("kanton_") or column_name.startswith("type_") or column_name.startswith("Availability_"):
            pass
        else:
            user_inputs[column_name] = st.number_input(f"Enter {column_name}")
    kanton = st.selectbox(f"Select Canton", kanton_list)
    type_unified = st.selectbox(f"Select Type", type_unified_list)
    availability = st.selectbox(f"Select Availability", availability_list)
  
    submit_button = st.form_submit_button('Submit')

    if submit_button:
        if 'result_df' in locals():
            del result_df
        df_kanton = pd.DataFrame({col: [1] if col == f"kanton_{kanton}" else [0] for col in column_names if col.startswith("kanton_")})
        df_type_unified = pd.DataFrame({col: [1] if col == f"type_unified_{type_unified}" else [0] for col in column_names if col.startswith("type_unified_")})
        df_availability = pd.DataFrame({col: [1] if col == f"Availability_Categorized_{availability}" else [0] for col in column_names if col.startswith("Availability_Categorized_")})
        df_user_inputs = pd.DataFrame([user_inputs])
        df = pd.DataFrame([user_inputs])
        df = df.replace(0.0, np.nan)
        result_df = pd.concat([df, df_kanton, df_type_unified, df_availability], axis=1)
        prediction = 0
        prediction = predict(loaded_model, result_df)
        # change locale to CHF
        locale.setlocale(locale.LC_ALL, 'de_CH.UTF-8')
        prediction_local = locale.format_string('%.2f', prediction[0], True)
        st.write(f'Predicted Price: {prediction_local} CHF')
        st.write(result_df)
        
