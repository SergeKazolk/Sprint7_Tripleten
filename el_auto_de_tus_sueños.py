# Importamos librerías que se usan
import streamlit as st
import pandas as pd

df = pd.read_csv('vehicles_us_limpio.csv')

# Configuración de la página
st.set_page_config(page_title='El auto de tus sueños', layout='wide')


# Título y descripción
st.title("🚗 El auto de tus sueños")
st.subheader("Filtra para encontrar justo lo que necesitas")

# Filtros
st.sidebar.header("Filtros")

# Marcas
marcas = df['Marca'].dropna().unique()
marca = st.sidebar.multiselect("Marca", sorted(marcas))

# Modelos
modelos = df['Modelo'].dropna().unique()
modelo = st.sidebar.multiselect("Modelo", sorted(modelos))

# Año
años = sorted(df['Año del modelo'].dropna().unique())
año = st.sidebar.multiselect("Año del modelo", años)

# Precio
min_precio = int(df['Precio'].min())
max_precio = int(df['Precio'].max())
rango_precio = st.sidebar.slider(
    "Rango de precio", min_precio, max_precio, (min_precio, max_precio))

# Estrellas de condición
condiciones = df['Condición'].dropna().unique()
condicion = st.sidebar.multiselect("Condición", sorted(condiciones))

# Tipo
tipos = df['Tipo'].dropna().unique()
tipo = st.sidebar.multiselect("Tipo", sorted(tipos))

# Cilindrada
cilindradas = df['Cilindrada'].dropna().unique()
cilindrada = st.sidebar.multiselect("Cilindrada", sorted(cilindradas))

# Transmisión
transmisiones = df['Transmisión'].dropna().unique()
transmision = st.sidebar.multiselect("Transmisión", sorted(transmisiones))

# Aplicar filtrado
df_filtrado = df.copy()

# Aplicación activa del filtrado
if marca:
    df_filtrado = df_filtrado[df_filtrado['Marca'].isin(marca)]
if modelo:
    df_filtrado = df_filtrado[df_filtrado['Modelo'].isin(modelo)]
if año:
    df_filtrado = df_filtrado[df_filtrado['Año del modelo'].isin(año)]
if condicion:
    df_filtrado = df_filtrado[df_filtrado['Condición'].isin(condicion)]
if tipo:
    df_filtrado = df_filtrado[df_filtrado['Tipo'].isin(tipo)]
if cilindrada:
    df_filtrado = df_filtrado[df_filtrado['Cilindrada'].isin(cilindrada)]
if transmision:
    df_filtrado = df_filtrado[df_filtrado['Transmisión'].isin(transmision)]

# Filtrado por precio
df_filtrado = df_filtrado[
    (df_filtrado['Precio'] >= rango_precio[0]) &
    (df_filtrado['Precio'] <= rango_precio[1])
]

# Muestra del resultado
st.subheader("Resultados de la búsqueda")
st.write(f"Se encontraron {df_filtrado.shape[0]} coincidencias")
st.dataframe(df_filtrado)


# Acceso a todo el catálogo
# st.subheader('Catálogo de autos disponibles')
# st.dataframe(df)
