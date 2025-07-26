import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV (ajustar la ruta si es necesario)
car_data = pd.read_csv('../vehicles_us.csv')

# Encabezado de la app
st.header('Análisis de anuncios de vehículos en Estados Unidos de América.')

# Botón: construir histograma
hist_button = st.button('Construir histograma del odómetro')

if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    fig = px.histogram(car_data, x='odometer', nbins=30,
                       title='Distribución del odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón: construir gráfico de dispersión
scatter_button = st.button(
    'Construir gráfico de dispersión: precio vs odómetro')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: "odometer" vs "price"')
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Precio vs Odómetro',
                     labels={'odometer': 'Odómetro', 'price': 'Precio'})
    st.plotly_chart(fig, use_container_width=True)
