import streamlit as st

# if in directory, start the app from terminal with: streamlit run ./home.py
st.title('Immo-Calculator')
st.subheader('Instructions')
st.write("""
         Welcome to our Immo-Calculator. 
         This is a simple tool to predict the price of a property.
         Choose your model in the navigation bar based on your available information. 
         The simple regression will only need the living space of the property. The expert model will need more information.
         """)