import streamlit as st
import pandas as pd
import prediction
from combined_attributes_adder import CombinedAttributesAdder
from sklearn.base import BaseEstimator, TransformerMixin

st.title('End2End')

# Barra lateral izquierda
with st.sidebar:

    # Información geográfica
    longitude = st.number_input('Length', min_value = -124.0, max_value = -110.0, format = "%.2f")
    latitude = st.number_input('Latitude', min_value = 30.0, max_value = 50.0, format = "%.2f")
    total_rooms = st.number_input('Total Rooms', min_value = 1.0, max_value = 50000.0, format = "%.0f")
    total_bedrooms = st.number_input('Total Bedrooms', min_value = 1.0, max_value = 7000.0, format = "%.0f")

    # Características adicionales
    population = st.number_input('Population', min_value = 1.0, max_value = 50000.0, format = "%.0f")
    ocean_proximity = st.selectbox('Ocean Proximity', ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'])

    # Predicción
    households = st.number_input('Households', min_value = 1.0, max_value = 10000.0, format = "%.0f")
    housing_median_age = st.number_input('Housing median age', step=1.0, min_value=1.0, max_value=100.0, format = "%.0f")
    median_income = st.number_input('Median income', min_value = 0.0, max_value = 17.0, format = "%.4f")

# Contenido principal
with st.container():

    

    # Muestra el resultado de la predicción
    if st.button('Prediction'):
        data = pd.DataFrame({
            'longitude': [longitude],
            'latitude': [latitude],
            'housing_median_age': [housing_median_age],
            'total_rooms': [total_rooms],
            'total_bedrooms': [total_bedrooms],
            'population': [population],
            'households': [households],
            'median_income': [median_income],
            'ocean_proximity': [ocean_proximity]}
        )

        result = prediction.predict(data)
        st.write("Valor predecido es de {:.1f} dlls".format(result[0]))

# Cambiar la fuente a Roboto
st.markdown('<style>body { font-family: Roboto, sans-serif; } </style>', unsafe_allow_html=True)
