import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Datos de ejemplo (ajusta con tus datos específicos)
x = np.arange(1, 6)
y1 = np.random.randint(10, 50, size=5)
y2 = np.random.randint(5, 40, size=5)

# Crear un dashboard con varios gráficos
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Configurar fondo blanco para todo el dashboard
fig.patch.set_facecolor('white')

# Gráfico 1: Línea
axs[0, 0].plot(x, y1, marker='o', label='Serie 1', color='blue')
axs[0, 0].set_title("¿Cuál es la tendencia de la Serie 1?")
axs[0, 0].set_xlabel("X")
axs[0, 0].set_ylabel("Y")
axs[0, 0].legend()
axs[0, 0].grid(True)

# Gráfico 2: Barras
axs[0, 1].bar(x, y1, color='green', label='Barras 1')
axs[0, 1].set_title("¿Cómo se comparan los valores de la Serie 1?")
axs[0, 1].set_xlabel("X")
axs[0, 1].set_ylabel("Y")
axs[0, 1].legend()

# Gráfico 3: Línea alternativa
axs[1, 0].plot(x, y2, marker='s', linestyle='--', label='Serie 2', color='red')
axs[1, 0].set_title("¿Cuál es la tendencia de la Serie 2?")
axs[1, 0].set_xlabel("X")
axs[1, 0].set_ylabel("Y")
axs[1, 0].legend()
axs[1, 0].grid(True)

# Gráfico 4: Barras alternativas
axs[1, 1].bar(x, y2, color='orange', label='Barras 2')
axs[1, 1].set_title("¿Cómo se comparan los valores de la Serie 2?")
axs[1, 1].set_xlabel("X")
axs[1, 1].set_ylabel("Y")
axs[1, 1].legend()

# Ajustar diseño general y márgenes
plt.tight_layout()
plt.show()
