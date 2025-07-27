import streamlit as st
import pandas as pd
from PIL import Image

# Configuración de página
st.set_page_config(layout="wide")

# Carga de datos con caché para evitar recarga innecesaria


@st.cache_data
def cargar_datos():
    return pd.read_csv('vehicles_us_limpio.csv')


df = cargar_datos()

# Inicializar estado de filtros si no existen aún
filtros = ['condicion', 'marca', 'modelo',
           'año', 'tipo', 'cilindrada', 'transmision']
for key in filtros:
    if key not in st.session_state:
        st.session_state[key] = []

if "rango_precio" not in st.session_state:
    st.session_state["rango_precio"] = (
        int(df["Precio"].min()), int(df["Precio"].max()))


# Botón para limpiar filtros
if st.sidebar.button("🧹 Limpiar filtros"):
    for key in filtros:
        st.session_state[key] = []
    st.session_state["rango_precio"] = (
        int(df["Precio"].min()), int(df["Precio"].max()))


# Copia para filtrar progresivamente
filtro_actual = df.copy()

# Texto centrado con markdown y HTML
st.markdown("""
    <h3 style='text-align: center;'>¡Comienza a elegir! ¡Prueba los filtros!</h3>
    <h4 style='text-align: center;'>El AUTO DE TUS SUEÑOS está a unos clicks de distancia</h4>
""", unsafe_allow_html=True)

# Imagen centrada con columnas
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("img/auto_interrogacion.png", width=400)

# --- SIDEBAR ---
st.sidebar.header("Filtros")

# --- Filtro Condición ---
condicion_opciones = sorted(filtro_actual['Condición'].dropna().unique())
condicion = st.sidebar.multiselect(
    "Condición", condicion_opciones, key='condicion')
if condicion:
    filtro_actual = filtro_actual[filtro_actual['Condición'].isin(condicion)]

# --- Filtro Marca ---
marca_opciones = sorted(filtro_actual['Marca'].dropna().unique())
marca = st.sidebar.multiselect("Marca", marca_opciones, key='marca')
if marca:
    filtro_actual = filtro_actual[filtro_actual['Marca'].isin(marca)]

# --- Filtro Modelo ---
modelo_opciones = sorted(filtro_actual['Modelo'].dropna().unique())
modelo = st.sidebar.multiselect("Modelo", modelo_opciones, key='modelo')
if modelo:
    filtro_actual = filtro_actual[filtro_actual['Modelo'].isin(modelo)]

# --- Filtro Año del modelo ---
año_opciones = sorted(filtro_actual['Año del modelo'].dropna().unique())
año = st.sidebar.multiselect("Año del modelo", año_opciones, key='año')
if año:
    filtro_actual = filtro_actual[filtro_actual['Año del modelo'].isin(año)]

# --- Filtro Tipo ---
tipo_opciones = sorted(filtro_actual['Tipo'].dropna().unique())
tipo = st.sidebar.multiselect("Tipo", tipo_opciones, key='tipo')
if tipo:
    filtro_actual = filtro_actual[filtro_actual['Tipo'].isin(tipo)]

# --- Filtro Cilindrada ---
cilindrada_opciones = sorted(filtro_actual['Cilindrada'].dropna().unique())
cilindrada = st.sidebar.multiselect(
    "Cilindrada", cilindrada_opciones, key='cilindrada')
if cilindrada:
    filtro_actual = filtro_actual[filtro_actual['Cilindrada'].isin(cilindrada)]

# --- Filtro Transmisión ---
transmision_opciones = sorted(filtro_actual['Transmisión'].dropna().unique())
transmision = st.sidebar.multiselect(
    "Transmisión", transmision_opciones, key='transmision')
if transmision:
    filtro_actual = filtro_actual[filtro_actual['Transmisión'].isin(
        transmision)]

# --- Filtro Precio ---
min_precio = int(df['Precio'].min())
max_precio = int(df['Precio'].max())

# Slider sin modificar session_state directamente
rango_precio = st.sidebar.slider(
    "Rango de precio",
    min_value=min_precio,
    max_value=max_precio,
    value=(min_precio, max_precio),
    key="rango_precio"
)

# Aplicar filtro
filtro_actual = filtro_actual[
    (filtro_actual["Precio"] >= rango_precio[0]) &
    (filtro_actual["Precio"] <= rango_precio[1])
]


# --- Control de número de resultados mostrados ---
max_resultados = st.sidebar.slider(
    "Máximo de resultados a mostrar", 5, 100, 50)
df_vista = filtro_actual.head(max_resultados)

# --- Mostrar resultados filtrados ---
filtros_aplicados = any([
    condicion, marca, modelo, año, tipo, cilindrada, transmision,
    rango_precio != (min_precio, max_precio)
])

if filtros_aplicados:
    st.subheader("Resultados de la búsqueda")

    if filtro_actual.empty:
        st.warning("No se encontraron resultados con los filtros seleccionados.")
    else:
        # Mostrar estrellas doradas para condición
        def estrellas_html(cond):
            estrellas = len(cond.strip("*"))
            return f"<span style='color:gold'>{'★'*estrellas}</span>"

        if len(df_vista) <= 50:
            df_vista['Condición'] = df_vista['Condición'].apply(estrellas_html)
            st.markdown(
                df_vista.to_html(escape=False, index=False),
                unsafe_allow_html=True
            )
        else:
            st.dataframe(df_vista)

# --- Catálogo completo (comentado por ahora) ---
# st.subheader("Catálogo completo")
# st.dataframe(df)
