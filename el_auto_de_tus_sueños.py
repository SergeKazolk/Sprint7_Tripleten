import streamlit as st
import pandas as pd
from PIL import Image

# Configuración de página
st.set_page_config(layout="wide")

# Carga de datos con caché


@st.cache_data
def cargar_datos():
    return pd.read_csv('vehicles_us_limpio_2.csv')


df = cargar_datos()

# Inicializar estado de filtros si no existen
filtros = ['condicion', 'marca', 'modelo',
           'año', 'tipo', 'cilindrada', 'transmision']
for key in filtros:
    if key not in st.session_state:
        st.session_state[key] = []

if "rango_precio" not in st.session_state:
    st.session_state["rango_precio"] = (
        int(df["Precio"].min()), int(df["Precio"].max()))

if "seleccion_auto" not in st.session_state:
    st.session_state.seleccion_auto = None

if "mostrar_confirmacion" not in st.session_state:
    st.session_state.mostrar_confirmacion = False

if "compra_confirmada" not in st.session_state:
    st.session_state.compra_confirmada = False

# Botón para limpiar filtros
if st.sidebar.button("🧹 Limpiar filtros"):
    for key in filtros:
        st.session_state[key] = []
    st.session_state["rango_precio"] = (
        int(df["Precio"].min()), int(df["Precio"].max()))

# Copia para filtrar progresivamente
filtro_actual = df.copy()

# Texto inicial e imagen
st.markdown("""
    <h3 style='text-align: center;'>¡Comienza a elegir! ¡Prueba los filtros!</h3>
    <h4 style='text-align: center;'>El AUTO DE TUS SUEÑOS está a unos clicks de distancia</h4>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("img/auto_interrogacion.png", width=700)

# Filtros en sidebar
st.sidebar.header("Filtros")

condicion_opciones = sorted(filtro_actual['Condición'].dropna().unique())
condicion = st.sidebar.multiselect(
    "Condición", condicion_opciones, key='condicion')
if condicion:
    filtro_actual = filtro_actual[filtro_actual['Condición'].isin(condicion)]

marca_opciones = sorted(filtro_actual['Marca'].dropna().unique())
marca = st.sidebar.multiselect("Marca", marca_opciones, key='marca')
if marca:
    filtro_actual = filtro_actual[filtro_actual['Marca'].isin(marca)]

modelo_opciones = sorted(filtro_actual['Modelo'].dropna().unique())
modelo = st.sidebar.multiselect("Modelo", modelo_opciones, key='modelo')
if modelo:
    filtro_actual = filtro_actual[filtro_actual['Modelo'].isin(modelo)]

año_opciones = sorted(filtro_actual['Año del modelo'].dropna().unique())
año = st.sidebar.multiselect("Año del modelo", año_opciones, key='año')
if año:
    filtro_actual = filtro_actual[filtro_actual['Año del modelo'].isin(año)]

tipo_opciones = sorted(filtro_actual['Tipo'].dropna().unique())
tipo = st.sidebar.multiselect("Tipo", tipo_opciones, key='tipo')
if tipo:
    filtro_actual = filtro_actual[filtro_actual['Tipo'].isin(tipo)]

cilindrada_opciones = sorted(filtro_actual['Cilindrada'].dropna().unique())
cilindrada = st.sidebar.multiselect(
    "Cilindrada", cilindrada_opciones, key='cilindrada')
if cilindrada:
    filtro_actual = filtro_actual[filtro_actual['Cilindrada'].isin(cilindrada)]

transmision_opciones = sorted(filtro_actual['Transmisión'].dropna().unique())
transmision = st.sidebar.multiselect(
    "Transmisión", transmision_opciones, key='transmision')
if transmision:
    filtro_actual = filtro_actual[filtro_actual['Transmisión'].isin(
        transmision)]

min_precio = int(df['Precio'].min())
max_precio = int(df['Precio'].max())
rango_precio = st.sidebar.slider("Rango de precio", min_value=min_precio,
                                 max_value=max_precio, value=st.session_state.rango_precio, key='rango_precio')

filtro_actual = filtro_actual[(filtro_actual["Precio"] >= rango_precio[0]) & (
    filtro_actual["Precio"] <= rango_precio[1])]

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
    st.caption(
        f"Mostrando {len(df_vista)} de {len(filtro_actual)} resultados disponibles")

    if filtro_actual.empty:
        st.warning("No se encontraron resultados con los filtros seleccionados.")
    else:
        # Mostrar estrellas doradas para condición
        def estrellas_html(cond):
            estrellas = len(cond.strip("*"))
            return f"<span style='color:gold'>{'★'*estrellas}</span>"

        df_vista_visual = df_vista.copy()
        df_vista_visual['Condición'] = df_vista_visual['Condición'].apply(
            estrellas_html)

        if len(df_vista_visual) <= 50:
            st.markdown(
                df_vista_visual.to_html(escape=False, index=False),
                unsafe_allow_html=True
            )
        else:
            st.dataframe(df_vista_visual)

        # Agregar selección después de mostrar resultados
        opciones_autos = df_vista.apply(
            lambda row: f"{row['Marca']} {row['Modelo']} {row['Año del modelo']} - ${row['Precio']}", axis=1
        ).tolist()

        seleccion = st.selectbox("Selecciona un auto para continuar:", [
                                 "-- Elige uno --"] + opciones_autos)

        if seleccion != "-- Elige uno --":
            st.session_state.seleccion_auto = seleccion
            st.session_state.mostrar_confirmacion = True

# Mostrar ficha técnica y confirmación de compra
if st.session_state.mostrar_confirmacion and st.session_state.seleccion_auto:
    st.markdown("## Ficha técnica del auto seleccionado")

    idx = df_vista[
        df_vista.apply(
            lambda row: f"{row['Marca']} {row['Modelo']} {row['Año del modelo']} - ${row['Precio']}",
            axis=1
        ) == st.session_state.seleccion_auto
    ].index

    if not idx.empty:
        auto_ficha = df_vista.loc[idx[0]]
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("img/auto_interrogacion_2.jpg", width=350)
        with col2:
            st.markdown(
                f"### {auto_ficha['Marca']} {auto_ficha['Modelo']} ({auto_ficha['Año del modelo']})")
            st.markdown(f"**Precio:** ${auto_ficha['Precio']}")
            st.markdown(f"**Condición:** {auto_ficha['Condición']}")
            st.markdown(f"**Cilindrada:** {auto_ficha['Cilindrada']}")
            st.markdown(f"**Combustible:** {auto_ficha['Combustible']}")
            st.markdown(f"**Kilometraje:** {auto_ficha['Kilometraje']} km")
            st.markdown(f"**Transmisión:** {auto_ficha['Transmisión']}")
            st.markdown(f"**Tipo:** {auto_ficha['Tipo']}")
            st.markdown(f"**4WD:** {auto_ficha['4WD']}")
            st.markdown(f"**Color:** {auto_ficha['Color']}")
            st.markdown(
                f"**Publicado:** {str(auto_ficha['Fecha de posteo']).split(' ')[0]}")

    st.markdown("### ¿Deseas comprar este auto?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Sí, comprar"):
            st.session_state.compra_confirmada = True
            st.session_state.mostrar_confirmacion = False
    with col2:
        if st.button("❌ No, seguir buscando"):
            st.session_state.seleccion_auto = None
            st.session_state.mostrar_confirmacion = False
            st.session_state.compra_confirmada = False

if st.session_state.compra_confirmada:
    st.success("🎉 ¡Felicidades! El auto de tus sueños es tuyo.")
