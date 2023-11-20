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

# xgb model
import xgboost as xgb
from xgboost import XGBRegressor
locale.setlocale(locale.LC_ALL, 'de_CH.UTF-8')
df_raw = pd.read_csv('../../../../data/immo_data_clean.csv', low_memory=False)
# Identify columns with object dtype
categorical_columns = df_raw.select_dtypes(include=['object']).columns.tolist()

# Identify columns with numerical dtype
numerical_columns = df_raw.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Convert to dummy variables
df_raw = pd.get_dummies(df_raw, columns=categorical_columns, drop_first=True, dtype=int)
df = df_raw.copy()

# Compute the 1% and 99% quantiles for each numerical column
quantiles_1 = df[numerical_columns].quantile(0.015)
quantiles_99 = df[numerical_columns].quantile(0.985)

# Replace outliers in the original data with NaN values
for column in numerical_columns:
    condition = (df[column] < quantiles_1[column]) | (df[column] > quantiles_99[column])
    df.loc[condition, column] = None

# Remove all na rows in the target column
df = df.dropna(subset=['price_cleaned'], axis=0)
train, test = train_test_split(df, test_size=0.2, random_state=42)

X_train = train.drop("price_cleaned", axis=1)
y_train = train["price_cleaned"]

X_test = test.drop("price_cleaned", axis=1)
y_test = test["price_cleaned"]
cols = X_train.columns

X_train_with_na = X_train.copy()
X_test_with_na = X_test.copy()

imputer = KNNImputer(n_neighbors=5)
X_train = pd.DataFrame(imputer.fit_transform(X_train), columns=cols)
X_test = pd.DataFrame(imputer.transform(X_test), columns=cols)
scaler = StandardScaler()
X_train = pd.DataFrame(scaler.fit_transform(X_train), columns=cols)
X_test = pd.DataFrame(scaler.transform(X_test), columns=cols)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def xgb_model(X_train, y_train, X_test, y_test, cv=5, max_depth=[12], learning_rate=[0.1], booster=['gbtree']):
    """ Creates a XGBoost model with grid search cv
    """
    xgb = XGBRegressor()

    param_grid = {
        'max_depth': max_depth,
        'learning_rate': learning_rate,
        'booster': booster,
        'random_state': [42]
    }

    grid_xgb = GridSearchCV(xgb, param_grid, cv=cv, n_jobs=5, scoring='neg_mean_absolute_percentage_error', verbose=1)

    grid_xgb.fit(X_train, y_train)

    return grid_xgb

model= xgb_model(
    X_train,
    y_train,
    X_test,
    y_test,
    cv=5,
    max_depth = [None, 6, 9, 12, 15],
    learning_rate = [0.1],
    booster = ['gbtree']
)

# create prediction function for above xgb model
def predict(model, X):
    return model.predict(X)

# make title
st.title('Immo-Calculator')

# make input fields
with st.form(key='my_form'):
    zip_code = st.number_input(label='Floor Space')
    year_built = st.selectbox('Year', range(1900, 2023))
    living_area_unified = st.number_input(label='SQM Living Space')
    Floor_unified = st.number_input(label='# Floors')
    Floor_space = st.number_input(label='Floor Space')
    Plot_area = st.number_input(label='Plot Area')
    Rooms = st.number_input(label='# Rooms')
    distance_to_station = st.number_input(label='Distance to Trainstation')
    type = st.selectbox('Type', ['Flat', 'House', 'Castle', 'Chalet','Villa','Rustico','Detached House','Loft','Studio'])
    municipality = st.text_input(label='Municipality')
    availability_category = st.selectbox('Availability', ['Immediately', 'By Agreement', 'Date (Specify later)'])
    availability_date = st.date_input(label='Availability Date')
    submit_button = st.form_submit_button('Submit')

    if submit_button:
        # make prediction
        X = pd.DataFrame({'zip_code': [zip_code], 'year_built': [year_built], 'living_area_unified': [living_area_unified], 'Floor_unified': [Floor_unified], 'Floor_space': [Floor_space], 'Plot_area': [Plot_area], 'Rooms': [Rooms], 'distance_to_station': [distance_to_station], 'type_House': [type], 'municipality': [municipality], 'availability_category': [availability_category], 'availability_date': [availability_date]})
        #prediction = predict(model, X)
        #prediction_local = locale.format_string('%.2f', prediction[0], True)
        #st.subheader(f'Predicted Price: {prediction_local} CHF')
        st.write(X)
        
