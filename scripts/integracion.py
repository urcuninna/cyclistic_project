'''
En este codigo voy a unir todos los archivos csv en
uno solo despues de haber validado que las columnas y tipos de datos son iguales
'''

import pandas as pd
import glob

ruta = glob.glob(
    r"C:\Users\ERIKA PINCHAO\OneDrive\Documentos\Data science\cyclistic_project\*.csv")
lista_df = [pd.read_csv(archivo) for archivo in ruta]
df_maestro = pd.concat(lista_df, ignore_index=True)
df_maestro.to_csv(
    r"C:\Users\ERIKA PINCHAO\OneDrive\Documentos\Data science\cyclistic_project\dataset_maestro_ciclistas.csv", index=False)

print("¡Archivo exportado con éxito!")
