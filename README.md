# ¿Qué hace exitosa una película en Netflix? 🎬📈
### Análisis y Segmentación Estratégica de Portafolio en Python

Este es un proyecto de análisis de datos orientado al negocio (Data Analytics & Business Strategy) diseñado para responder a preguntas clave sobre la inversión en contenido cinematográfico en plataformas de streaming como **Netflix**. 

El objetivo principal es identificar qué factores (género, presupuesto, calificaciones) influyen en el éxito de una producción y cómo segmentar el catálogo de forma óptima para maximizar el retorno de la inversión (ROI) y la retención de usuarios.

---

## 📌 Hallazgos Clave de Negocio
* **El dinero asegura vistas, no calidad**: Existe una correlación positiva extremadamente fuerte ($r = 0.87$) entre el presupuesto de una película y sus visualizaciones. Sin embargo, la correlación entre presupuesto y calificación es nula ($-0.08$), lo que demuestra que inyectar capital garantiza distribución y alcance, pero no el aprecio del usuario.
* **La estrategia de "La Larga Cola" (The Long Tail)**: El 46% de las películas en Netflix son producciones de bajo costo ($17.7M USD promedio) orientadas a nichos específicos. Aunque tienen pocas vistas individuales, registran el **mayor nivel de satisfacción general (7.3/10.0)**, siendo vitales para la retención del suscriptor.
* **Los documentales son el contenido más eficiente**: Tienen el menor costo de producción ($14M USD promedio) y, aunque capturan pocas vistas (13.9M), logran una puntuación récord de la audiencia de **8.3/10.0**.

---

## 📊 Visualizaciones Destacadas

### 1. Distribución de Inversión por Género
Los géneros de **Ciencia Ficción** y **Acción** concentran la mayor inversión de capital promedio, superando los $90M USD.

![Presupuesto Promedio por Género](budget_by_genre.png)

### 2. Impacto Financiero en las Visualizaciones
Un gráfico de dispersión revela cómo el presupuesto se traduce en vistas y cómo se agrupan los géneros comerciales frente a los de nicho.

![Relación Presupuesto vs Vistas](budget_vs_views.png)

---

## 📂 Estructura del Repositorio
* **[netflix_business_report.md](netflix_business_report.md)**: El informe de investigación completo estructurado bajo la perspectiva de Ingeniería Comercial, incluyendo marco teórico, hipótesis y referencias bibliográficas en formato **APA 7**.
* **[netflix_titles_extended.csv](netflix_titles_extended.csv)**: El dataset extendido con 250 registros y variables financieras/de visualización.
* **`budget_by_genre.png`** y **`budget_vs_views.png`**: Gráficos analíticos generados con Matplotlib y Seaborn.
* **`analisis.py`**: *(Tu script principal de Python)*.

---

## 💻 Resumen del Código Utilizado (Stack Tecnológico)
* **Python 3**
* **Pandas**: Para la manipulación, limpieza e imputación de nulos (usando medianas y etiquetas de control).
* **Matplotlib & Seaborn**: Para la generación de gráficos estéticos y personalización de ejes y paletas de colores.

---

## 🙋‍♂️ Autor
* **[Tu Nombre]** - Estudiante de Ingeniería Comercial.
* **LinkedIn**: [Tu Enlace a LinkedIn]
* **GitHub**: [Tu Enlace a GitHub]
