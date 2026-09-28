# ==================================================================
#  p086-acceder-lista.py
#  Listas en Python - Parte 1 | Ejemplo 1: Acceder elementos de una lista
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Se tiene una lista de mediciones numericas y se debe obtener:
#   - El numero total de mediciones.
#   - La primera y la ultima medicion registrada.
#   - Un subconjunto que va del tercer al sexto elemento.
#   - Los primeros tres y los ultimos tres registros.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista fija de mediciones (nums).
#  Proceso : len() para el total; indices positivos y negativos para
#            los extremos; slicing [ini:fin] para los subconjuntos.
#  Salida  : total, extremos y sub-listas impresas en pantalla.
# ==================================================================

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print("\033[2J\033[H", end="", flush=True)
print("Acceder a los elementos de una lista")
print("-" * 60)

print("\nLongitud y contenido de las mediciones:")
print(f"Cuantas mediciones son : {len(nums)}")
print(f"Todas las mediciones   : {nums}")

print("\nPor indice positivo:")
# El primer elemento es el indice 0 y el ultimo es len(nums) - 1
print(f"Primera y ultima : {nums[0]}, {nums[len(nums) - 1]}")

print("\nPor indice negativo:")
# -len(nums) es el primer elemento y -1 es el ultimo
print(f"Primera y ultima : {nums[-len(nums)]}, {nums[-1]}")

print("\nPor rango:")
# Tercer elemento = indice 2; sexto elemento = indice 5 (el 6 no se incluye)
print(f"Del tercer al sexto elemento [2:6] : {nums[2:6]}")

print("\nPrimeros y ultimos registros:")
print(f"Los primeros 3 [:3]  : {nums[:3]}")
print(f"Los ultimos 3  [-3:] : {nums[-3:]}")

print("\n\nGracias por utilizar este programa...")
