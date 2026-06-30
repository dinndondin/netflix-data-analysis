# ==============================================================================
# PROYECTO: ¿Qué hace exitosa una película en Netflix?
# Análisis y segmentación de portafolio para toma de decisiones
# Autora: Geraldine Ramos Cortés
# ==============================================================================

# ------------------------------------------------------------------------------
# A) Importar librerías
# ------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración estética para los gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# ------------------------------------------------------------------------------
# B) Lectura del dataset
# ------------------------------------------------------------------------------
print("1. Cargando datos...")
df = pd.read_csv("netflix_titles_extended.csv")

# ------------------------------------------------------------------------------
# C) Limpieza y Calidad de Datos
# ------------------------------------------------------------------------------
print("\n2. Limpiando y preparando datos...")

# Corregir error de codificación en el nombre de la columna del año
df.rename(columns={"ao_lanzamiento": "anio_lanzamiento"}, inplace=True)

# Imputar valores nulos en variables de texto (categóricas)
df["director"] = df["director"].fillna("Desconocido")
df["pais"] = df["pais"].fillna("Desconocido")

# Imputar valores nulos en variables numéricas utilizando la mediana
mediana_presupuesto = df["presupuesto_millones"].median()
df["presupuesto_millones"] = df["presupuesto_millones"].fillna(mediana_presupuesto)

mediana_puntaje = df["puntaje_audiencia"].median()
df["puntaje_audiencia"] = df["puntaje_audiencia"].fillna(mediana_puntaje)

# Eliminar duplicados si existieran
df.drop_duplicates(inplace=True)

print(f"-> Datos limpios. Dimensiones finales: {df.shape[0]} filas y {df.shape[1]} columnas.")

# ------------------------------------------------------------------------------
# D) Análisis Exploratorio de Datos (EDA)
# ------------------------------------------------------------------------------
print("\n3. Corriendo Análisis Exploratorio (EDA)...")

# Estadísticas descriptivas de las columnas numéricas
print("\n--- Resumen Estadístico General ---")
print(df.describe().round(2))

# Rendimiento por género
print("\n--- Métricas Promedio por Género ---")
rendimiento_genero = df.groupby("genero")[["vistas_millones", "presupuesto_millones", "puntaje_audiencia"]].mean().round(2)
print(rendimiento_genero)

# Matriz de Correlación de Pearson
print("\n--- Matriz de Correlación ---")
matriz_corr = df[["presupuesto_millones", "vistas_millones", "puntaje_audiencia"]].corr().round(2)
print(matriz_corr)

# ------------------------------------------------------------------------------
# E) Visualización de Datos (Guardado de gráficos)
# ------------------------------------------------------------------------------
print("\n4. Generando visualizaciones...")

# Gráfico 1: Presupuesto promedio por género (Barras)
plt.figure(figsize=(10, 6))
order_genres = df.groupby('genero')['presupuesto_millones'].mean().sort_values(ascending=False).index
sns.barplot(
    data=df, 
    x="genero", 
    y="presupuesto_millones", 
    hue="genero", 
    order=order_genres, 
    legend=False, 
    palette="magma"
)
plt.title("Presupuesto Promedio de Producción por Género en Netflix", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Género de Película", fontsize=12)
plt.ylabel("Presupuesto Promedio (Millones de USD)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("budget_by_genre.png", dpi=300)
plt.close()
print("-> Gráfico 'budget_by_genre.png' guardado con éxito.")

# Gráfico 2: Presupuesto vs Vistas (Dispersión)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, 
    x="presupuesto_millones", 
    y="vistas_millones", 
    hue="genero", 
    style="genero", 
    s=100, 
    alpha=0.85, 
    palette="bright"
)
plt.title("Impacto de la Inversión: Presupuesto vs Visualizaciones en Netflix", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Presupuesto de Producción (Millones de USD)", fontsize=12)
plt.ylabel("Vistas Estimadas (Millones)", fontsize=12)
plt.legend(title="Géneros", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("budget_vs_views.png", dpi=300)
plt.close()
print("-> Gráfico 'budget_vs_views.png' guardado con éxito.")

# ------------------------------------------------------------------------------
# F) Segmentación de Portafolio
# ------------------------------------------------------------------------------
print("\n5. Aplicando segmentación de portafolio...")

# Definición de límites basados en las medianas
limite_presupuesto = 30.88
limite_vistas = 26.24

def clasificar_portafolio(fila):
    presupuesto = fila["presupuesto_millones"]
    vistas = fila["vistas_millones"]
    
    if presupuesto > limite_presupuesto and vistas > limite_vistas:
        return "Blockbuster Exitoso"
    elif presupuesto <= limite_presupuesto and vistas > limite_vistas:
        return "Joya Rentable (Viral)"
    elif presupuesto > limite_presupuesto and vistas <= limite_vistas:
        return "Alto Riesgo (Bajo Impacto)"
    else:
        return "Contenido de Nicho"

# Aplicar la función a cada fila del DataFrame
df["segmento"] = df.apply(clasificar_portafolio, axis=1)

# Mostrar distribución final
print("\n--- Distribución del Catálogo por Segmento ---")
print(df["segmento"].value_counts())

# Resumen de métricas de negocio por segmento
print("\n--- Métricas de Negocio por Segmento ---")
resumen_segmentos = df.groupby("segmento")[["vistas_millones", "presupuesto_millones", "puntaje_audiencia"]].mean().round(2)
print(resumen_segmentos)

