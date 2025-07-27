#  El auto de tus sueños

**"El auto de tus sueños"** es una aplicación interactiva desarrollada con Streamlit que te permite explorar y seleccionar vehículos usados disponibles en un catálogo limpio y filtrable. Los usuarios pueden aplicar filtros personalizados, visualizar resultados en tiempo real, consultar la ficha técnica de cada vehículo, simular una compra y analizar el comportamiento de los precios mediante visualizaciones gráficas.

##  Requisitos

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

##  Tecnologías utilizadas

- **Python 3.8+**
- [Streamlit](https://streamlit.io/)
- pandas
- matplotlib
- seaborn
- Pillow

##  ¿Cómo ejecutar la app?

```bash
streamlit run nombre_del_script.py
```

(Nota: reemplaza `nombre_del_script.py` con el nombre del archivo principal, por ejemplo, `el_auto_de_tus_sueños.py`)

##  Funcionalidades principales

- Filtros dinámicos por marca, modelo, año, tipo, condición, cilindrada, transmisión y precio.
- Visualización inmediata de los resultados en tabla.
- Selección de un vehículo y muestra de ficha técnica.
- Confirmación de compra simulada.
- Visualizaciones interactivas:
  - Histograma de precios.
  - Gráficos de dispersión seleccionables:
    - Precio vs. Marca
    - Precio vs. Año del modelo
    - Precio vs. Kilometraje
    - Precio vs. Cilindrada

##  Recursos

- Imágenes de apoyo ubicadas en la carpeta `/img`.

##  Estructura sugerida del proyecto

```
auto-de-tus-suenos/
│
├── vehicles_us_limpio_2.csv         # Archivo de datos limpio
├── el_auto_de_tus_suenos.py         # Archivo principal de Streamlit
├── requirements.txt                 # Dependencias del proyecto
├── README.md                        # Este archivo
└── img/
    ├── auto_interrogacion.png
    └── auto_interrogacion_2.jpg
```

##  Licencia

Proyecto educativo/descriptivo. Puedes adaptarlo y mejorarlo según tus necesidades.
