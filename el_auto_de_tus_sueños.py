# Importamos librerías que se usan
import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title='El auto de tus sueños', layout='wide')

# Carga de datos y optimización de uso


@st.cache_data
def cargar_datos():
    return pd.read_csv('vehicles_us_limpio.csv', parse_dates=['Fecha de posteo'])


df = cargar_datos()

# Título y descripción
st.title('🚗 El auto de tus sueños')
st.markdown('Explora y encuentra el auto usado ideal para ti.')

# Acceso al catálogo
st.subheader('Catálogo de autos disponibles')
st.dataframe(df)
