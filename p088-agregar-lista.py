# ==================================================================
#  p088-agregar-lista.py
#  Listas en Python - Parte 1 | Ejemplo 3: Agregar elementos a una lista
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Se recolectan datos de temperatura. Se debe:
#   - Anadir dos nuevas lecturas al final de la lista.
#   - Insertar una lectura corregida en una posicion especifica.
#   - Incorporar un lote completo de lecturas de otro sensor.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista inicial de temperaturas y lista del otro sensor.
#  Proceso : append() agrega al final; insert(pos, valor) inserta en
#            una posicion; extend(otra_lista) fusiona las listas.
#  Salida  : la lista despues de cada operacion.
# ==================================================================

nums = [80.3, 12.5, 60.2, 30.4]

print("\033[2J\033[H", end="", flush=True)
print("Agregar elementos a una lista")
print("-" * 60)

print(f"\nDatos iniciales: {nums}\n")

print("Agregar 90 y 100 al final (append):")
nums.append(90)
nums.append(100)
print(f"Resultado : {nums}\n")

print("Insertar 80 en la posicion 4 (insert):")
nums.insert(4, 80)
print(f"Resultado : {nums}\n")

print("Extender datos agregando [110, 120, 130] al final (extend):")
otros = [110, 120, 130]
nums.extend(otros)
print(f"Resultado : {nums}")

print("\n\nGracias por utilizar este programa...")
