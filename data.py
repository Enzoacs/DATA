# MicroProyecto de visualización de Datos en Python
# Utilizando Numpy, Pandas, Matplotlib e importando archivos Excel

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display
from tabulate import tabulate

# ============================
# Series
# ============================
Redes = pd.Series([1,2,3,4,5], index=["Instagram","Facebook","Twitter","LinkedIn","TikTok"])
print(Redes["Instagram"])  # Valor asociado a "Instagram"

# ============================
# DataFrame de ejemplo
# ============================
Redes = pd.DataFrame({
    "APP": ["Instagram","Facebook","Twitter","LinkedIn","TikTok"],
    "TOP": [1,2,3,4,5],
    "Fecha Creacion": ["06/10/2010.","04/02/2004.","21/03/2006.","05/05/2003.","01/09/2016."]
})

display(Redes)  # O print(Redes)

# ============================
# Importar Excel
# ============================
df1 = pd.read_excel("C:/Users/DELL/Desktop/TABLA_IA_NUMERICA.xlsx")

pd.set_option("display.max_columns", None)

print(df1)
print("Cantidad de filas y columnas:", df1.shape)

print("\nPrimera IA en el DataFrame:\n")
print(df1.head(1))

print("\nÚltima IA en el DataFrame:\n")
print(df1.tail(1))

# ============================
# Visualización estética
# ============================
print("\nDataFrame en formato tabulado:\n")
print(tabulate(df1, headers="keys", tablefmt="fancy_grid"))
print(df1.columns)

