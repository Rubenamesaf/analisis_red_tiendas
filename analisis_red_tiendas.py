import pandas as pd
import numpy as np

#Cargar los datos desde los archivos CSV

ventas_df = pd.read_csv('/workspace/ventas.csv')
inventarios_df = pd.read_csv('/workspace/inventarios.csv')
satisfaccion_df = pd.read_csv('/workspace/satisfaccion.csv')

#"""Limpieza de datos"""

ventas_df.dropna(inplace=True)
inventarios_df.dropna(inplace=True)
satisfaccion_df.dropna(inplace=True)

#"""Verificar estructuras"""

print("\n--- Información del DataFrame de Ventas ---")
print(ventas_df.info())
print("\n--- Información del DataFrame de Inventarios ---")
print(inventarios_df.info())
print("\n--- Información del DataFrame de Satisfacción ---")
print(satisfaccion_df.info())

#"""Exploración de datos:
#Ventas totales por producto y tienda

ventas_df['Total_Ventas'] = ventas_df['Unidades'] * ventas_df['Precio_unitario']
print("\n--- Ventas totales por tienda ---")
print(ventas_df.groupby('Tienda')['Total_Ventas'].sum())

#"""Resumen estadístico de ventas"""

print("\n--- Resumen estadístico de las ventas ---")
print(ventas_df['Total_Ventas'].describe())

#"""Promedio de ventas por tienda y categoría"""

print("\n--- Promedio de ventas por tienda y categoría ---")
print(ventas_df.groupby(['Tienda', 'Categoría'])['Total_Ventas'].mean())

#"""Análisis de inventarios: Rotación de inventarios"""

inventarios_df['Rotacion'] = ventas_df.groupby('Producto')['Unidades'].sum() / inventarios_df['Stock_Disponible']
print("\n--- Rotación de inventarios ---")
print(inventarios_df[['Producto', 'Rotacion']])

#"""Tiendas con niveles críticos de inventario (<10%)"""

inventarios_df['Porcentaje_Vendido'] = ventas_df.groupby('Producto')['Unidades'].sum() / inventarios_df['Stock_Disponible'] * 100
tiendas_criticas = inventarios_df[inventarios_df['Porcentaje_Vendido'] < 10]
print("\n--- Tiendas con niveles críticos de inventario ---")
print(tiendas_criticas)

#"""Análisis de satisfacción del cliente: Filtrar tiendas con satisfacción < 60%"""

tiendas_baja_satisfaccion = satisfaccion_df[satisfaccion_df['Satisfaccion'] < 60]
print("\n--- Tiendas con baja satisfacción del cliente ---")
print(tiendas_baja_satisfaccion)

#"""Cálculos con Numpy: Mediana y desviación estándar de ventas totales"""

ventas_totales_np = ventas_df['Total_Ventas'].to_numpy()
print("\n--- Mediana de las ventas totales ---")
print(np.median(ventas_totales_np))

print("\n--- Desviación estándar de las ventas totales ---")
print(np.std(ventas_totales_np))

#"""Simulación de proyecciones de ventas futuras"""

np.random.seed(42)
proyecciones_ventas = np.random.normal(np.mean(ventas_totales_np), np.std(ventas_totales_np), 100)
print("\n--- Proyecciones de ventas futuras (primeros 10 valores) ---")
print(proyecciones_ventas[:10])