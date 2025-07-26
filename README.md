# Sprint7_Tripleten
Proyecto sprint 7
# Proyecto: Análisis de Anuncios de Vehículos

Esta aplicación web fue creada con Streamlit. Permite analizar un conjunto de datos de anuncios de coches usados en Estados Unidos de América
### Funcionalidades EDA.ipynb
- Mostrar histograma del odómetro
- Mostrar gráfico de dispersión entre precio y odómetro

### Funcionalidades app.py
- Muestra los gráficos (histograma y gráfico de dispersión) interactivos y están construidos con Plotly.

### Funcionalidades datos_limpios.ipynb
-Carga el archivo vehicles_us.csv.
-Rellena valores faltantes de forma apropiada.

Transforma:

    *is_4wd: convierte a 'Sí', '-', 'No'.

    *model: se divide en Marca y Modelo con capitalización.

    *Columnas como Combustible, Condición, Color, Transmisión, Tipo, con nombres amigables en español.

-Renombra todas las columnas a títulos comprensibles.
-Convierte Fecha de posteo a tipo datetime.
-Guarda el nuevo archivo limpio como vehicles_us_limpio.csv.

### Funcionalidades "El auto de tus sueños.py"
