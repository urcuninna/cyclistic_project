"""
Este script procesa los datos de Cyclistic para el proyecto de Data Science.
Autor: Erika Pinchao
"""
import os
import pandas as pd

#Validación de nombres de columnas

ruta = r"C:\Users\ERIKA PINCHAO\OneDrive\Documentos\Data science\cyclistic_project"
archivos = [f for f in os.listdir(ruta) if f.endswith('.csv')]

ref = archivos[0]
df_ref = pd.read_csv(os.path.join(ruta, ref), nrows=1)
col_ref = set(df_ref.columns)

for archivo in archivos[1:]:
    df = pd.read_csv(os.path.join(ruta, archivo), nrows=0)
    col_actual = set(df.columns)
    if col_actual != col_ref:
        print(
            f'Las columnas del archivo {archivo} no coinciden con las del archivo de referencia {ref}.')
    else:
        print(
            f'Las columnas del archivo {archivo} coinciden con las del archivo de referencia {ref}.')
    
'''Hasta aqui llega el codigo de validacion de columnas, los nombres de las columnas son iguales en todos los archivos.'''

# Validación de tipos de datos

tipos_datos=df_ref.dtypes

for archivo in archivos[1:]:
    df = pd.read_csv(os.path.join(ruta, archivo), nrows=100)
    tipos_actuales = df.dtypes
    
    if not tipos_actuales.equals(tipos_datos):
        print(f"ERROR: {archivo} no coincide.")
        
        diferencias = tipos_actuales[tipos_actuales != tipos_datos]
        for col, tipo in diferencias.items():
            print(f"    - Columna '{col}': Es '{tipo}' pero debería ser '{tipos_datos[col]}'")
       
    else:
        print(f" {archivo} coincide correctamente.")

'''Hasta aqui llega el codigo de validacion de tipos de datos. Los meses 8 y 11 presentas errores
mes 8: start_station_name, end_station_name, start station_id y end_station_id deberian ser object y son float64
mes 11: end_station_name, end_station_id deberian ser object y son float64''' 