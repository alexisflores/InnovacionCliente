import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Intentar aplicar el estilo seaborn-whitegrid; usar default si no está disponible
try:
    plt.style.use('seaborn-whitegrid')
except OSError:
    plt.style.use('default')

# Datos simulados para las capacidades
data_sensing = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Datos Analizados (%)": [50, 65, 75, 80],
    "Meta Datos Analizados (%)": [60, 70, 80, 90],
    "Insights Generados": [10, 15, 20, 25],
    "Meta Insights Generados": [12, 18, 24, 30],
    "Tasa Respuesta (%)": [70, 75, 80, 85],
    "Meta Tasa Respuesta (%)": [75, 80, 85, 90],
}

data_seizing = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Usuarios Activos": [200, 300, 400, 500],
    "Meta Usuarios Activos": [250, 350, 450, 550],
    "Tasa de Conversión (%)": [20, 30, 35, 40],
    "Meta Tasa de Conversión (%)": [25, 35, 40, 50],
    "Funcionalidades Implementadas": [1, 2, 2, 3],
    "Meta Funcionalidades Implementadas": [1, 2, 3, 4],
}

data_configuring = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Capacidad Usuarios Concurrentes": [100, 150, 200, 250],
    "Meta Capacidad Usuarios Concurrentes": [120, 160, 220, 280],
    "Tiempo Inactividad (%)": [5, 4, 3, 2],
    "Meta Tiempo Inactividad (%)": [4, 3, 3, 2],
    "Precisión IA (%)": [70, 75, 80, 85],
    "Meta Precisión IA (%)": [75, 80, 85, 90],
}

# Transformar a DataFrames
df_sensing = pd.DataFrame(data_sensing)
df_seizing = pd.DataFrame(data_seizing)
df_configuring = pd.DataFrame(data_configuring)

# Configurar el título del tablero
st.title("Tablero de Control: Innovación Centrada en el Cliente")
st.markdown(
    """
    Este tablero muestra los KPIs organizados por metas y capacidades. Cada gráfico incluye los datos actuales
    y las metas respectivas para monitorear el progreso hacia los OKRs definidos.
    """
)

# Función para graficar KPIs con alternancia de tipos de gráficos
def plot_kpi(df, x_col, y_col, meta_col, title, xlabel, ylabel, chart_type="line"):
    fig, ax = plt.subplots(figsize=(8, 4))
    if chart_type == "line":
        ax.plot(df[x_col], df[y_col], marker='o', label='Actual', linewidth=2)
        ax.plot(df[x_col], df[meta_col], linestyle='--', label='Meta', color='red', linewidth=2)
    elif chart_type == "bar":
        ax.bar(df[x_col], df[y_col], label='Actual', color='skyblue', alpha=0.8)
        ax.plot(df[x_col], df[meta_col], linestyle='--', label='Meta', color='red', linewidth=2)
    elif chart_type == "stacked_bar":
        width = 0.4
        ax.bar(df[x_col], df[y_col], width, label='Actual', color='blue')
        ax.bar(df[x_col], df[meta_col], width, label='Meta', bottom=df[y_col], color='orange', alpha=0.6)
    
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.legend()
    st.pyplot(fig)

# Sección para Sensing
st.markdown("## Detección (Sensing)")
st.markdown(
    """
    ### OKR: Analizar datos y generar insights
    Este OKR busca mejorar el análisis de datos para identificar oportunidades de innovación y atender mejor
    las necesidades de los clientes.
    """
)

plot_kpi(df_sensing, "Periodo", "Datos Analizados (%)", "Meta Datos Analizados (%)",
         "Porcentaje de Datos Analizados", "Periodo", "Porcentaje", chart_type="line")
plot_kpi(df_sensing, "Periodo", "Insights Generados", "Meta Insights Generados",
         "Insights Generados", "Periodo", "Cantidad", chart_type="bar")
plot_kpi(df_sensing, "Periodo", "Tasa Respuesta (%)", "Meta Tasa Respuesta (%)",
         "Tasa de Respuesta", "Periodo", "Porcentaje", chart_type="line")

# Sección para Seizing
st.markdown("## Captación (Seizing)")
st.markdown(
    """
    ### OKR: Incrementar adopción y funcionalidades
    Este OKR está enfocado en aumentar la adopción de la plataforma myRAzept y desarrollar nuevas
    funcionalidades basadas en las necesidades del cliente.
    """
)

plot_kpi(df_seizing, "Periodo", "Usuarios Activos", "Meta Usuarios Activos",
         "Usuarios Activos", "Periodo", "Cantidad", chart_type="bar")
plot_kpi(df_seizing, "Periodo", "Tasa de Conversión (%)", "Meta Tasa de Conversión (%)",
         "Tasa de Conversión", "Periodo", "Porcentaje", chart_type="line")
plot_kpi(df_seizing, "Periodo", "Funcionalidades Implementadas", "Meta Funcionalidades Implementadas",
         "Funcionalidades Implementadas", "Periodo", "Cantidad", chart_type="stacked_bar")

# Sección para Configuring
st.markdown("## Configuración (Configuring)")
st.markdown(
    """
    ### OKR: Optimizar infraestructura digital
    Este OKR busca mejorar la capacidad tecnológica y la personalización de servicios a través de IA
    para optimizar la experiencia del cliente.
    """
)

plot_kpi(df_configuring, "Periodo", "Capacidad Usuarios Concurrentes", "Meta Capacidad Usuarios Concurrentes",
         "Capacidad de Usuarios Concurrentes", "Periodo", "Cantidad", chart_type="bar")
plot_kpi(df_configuring, "Periodo", "Tiempo Inactividad (%)", "Meta Tiempo Inactividad (%)",
         "Tiempo de Inactividad", "Periodo", "Porcentaje", chart_type="line")
plot_kpi(df_configuring, "Periodo", "Precisión IA (%)", "Meta Precisión IA (%)",
         "Precisión de IA", "Periodo", "Porcentaje", chart_type="line")

st.markdown("**Nota:** Los datos son simulados para ilustrar el tablero y no representan información real.")
