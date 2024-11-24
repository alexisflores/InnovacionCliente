import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos simulados
data_sensing = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Datos Analizados (%)": [50, 65, 75, 80],
    "Insights Generados": [10, 15, 20, 25],
    "Tasa Respuesta (%)": [70, 75, 80, 85],
}

data_seizing = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Usuarios Activos": [200, 300, 400, 500],
    "Tasa de Conversión (%)": [20, 30, 35, 40],
    "Funcionalidades Implementadas": [1, 2, 2, 3],
}

data_configuring = {
    "Periodo": ["Q1", "Q2", "Q3", "Q4"],
    "Capacidad Usuarios Concurrentes": [100, 150, 200, 250],
    "Tiempo Inactividad (%)": [5, 4, 3, 2],
    "Precisión IA (%)": [70, 75, 80, 85],
}

# Transformar a DataFrames
df_sensing = pd.DataFrame(data_sensing)
df_seizing = pd.DataFrame(data_seizing)
df_configuring = pd.DataFrame(data_configuring)

# Títulos
st.title("Tablero de Control: Innovación Centrada en el Cliente")
st.markdown("### Detección (Sensing)")

# Gráficos de Sensing
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(df_sensing["Periodo"], df_sensing["Datos Analizados (%)"], marker='o', label="Datos Analizados (%)")
ax[0].set_title("Datos Analizados")
ax[0].set_xlabel("Periodo")
ax[0].set_ylabel("Porcentaje")
ax[0].legend()

ax[1].bar(df_sensing["Periodo"], df_sensing["Insights Generados"], color='orange')
ax[1].set_title("Insights Generados")
ax[1].set_xlabel("Periodo")
ax[1].set_ylabel("Cantidad")

st.pyplot(fig)

# Captación (Seizing)
st.markdown("### Captación (Seizing)")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(df_seizing["Periodo"], df_seizing["Usuarios Activos"], marker='o', label="Usuarios Activos")
ax[0].set_title("Usuarios Activos")
ax[0].set_xlabel("Periodo")
ax[0].set_ylabel("Cantidad")
ax[0].legend()

ax[1].bar(df_seizing["Periodo"], df_seizing["Tasa de Conversión (%)"], color='green')
ax[1].set_title("Tasa de Conversión")
ax[1].set_xlabel("Periodo")
ax[1].set_ylabel("Porcentaje")

st.pyplot(fig)

# Configuración (Configuring)
st.markdown("### Configuración (Configuring)")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].bar(df_configuring["Periodo"], df_configuring["Capacidad Usuarios Concurrentes"], color='purple')
ax[0].set_title("Capacidad de Usuarios Concurrentes")
ax[0].set_xlabel("Periodo")
ax[0].set_ylabel("Cantidad")

ax[1].plot(df_configuring["Periodo"], df_configuring["Precisión IA (%)"], marker='o', label="Precisión IA (%)")
ax[1].set_title("Precisión de IA")
ax[1].set_xlabel("Periodo")
ax[1].set_ylabel("Porcentaje")
ax[1].legend()

st.pyplot(fig)

st.markdown("**Nota:** Los datos son ejemplos simulados para ilustrar el tablero.")
