# ==================================================================
#  p096-procesar-datos-sensores.py
#  Listas en Python - Parte 2 | Ejemplo 5: Procesar datos de sensores
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Dos sensores recogen 10 mediciones numericas cada uno:
#   - Generar dos listas con 10 numeros aleatorios (1 a 100) que
#     simulan los datos de cada sensor y mostrarlas.
#   - Transformar los datos elevando al cuadrado cada medicion.
#   - Crear una tercera lista con la suma de los datos transformados
#     de ambos sensores (posicion a posicion).
#   - Mostrar las listas transformadas y la lista combinada.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : datos simulados con random.randint(1, 100).
#  Proceso : for + append() para generar, transformar y combinar.
#  Salida  : listas originales, transformadas y combinada.
# ==================================================================

import random

print("\033[2J\033[H", end="", flush=True)
print("Procesamiento de datos de sensores")
print("-" * 60)

MEDICIONES = 10

# --- 1. Generacion de Datos Simulados ---
print("Simulando la recoleccion de datos de dos sensores...")
sensor_a_datos = []
sensor_b_datos = []

for _ in range(MEDICIONES):
    sensor_a_datos.append(random.randint(1, 100))   # Llena la lista del sensor A
    sensor_b_datos.append(random.randint(1, 100))   # Llena la lista del sensor B

print("\n--- Datos Originales de los Sensores ---")
print(f"Sensor A: {sensor_a_datos}")
print(f"Sensor B: {sensor_b_datos}")

# --- 2. Transformacion y Combinacion de Datos ---
sensor_a_transformado = []
sensor_b_transformado = []
datos_combinados = []
for i in range(MEDICIONES):
    a2 = sensor_a_datos[i] ** 2
    b2 = sensor_b_datos[i] ** 2
    sensor_a_transformado.append(a2)
    sensor_b_transformado.append(b2)
    datos_combinados.append(a2 + b2)

print("\n--- Datos Transformados (al cuadrado) ---")
print(f"Sensor A: {sensor_a_transformado}")
print(f"Sensor B: {sensor_b_transformado}")

print("\n--- Datos Combinados (A^2 + B^2) ---")
print(f"Combinado: {datos_combinados}")

print("\n\nGracias por utilizar este programa...")
