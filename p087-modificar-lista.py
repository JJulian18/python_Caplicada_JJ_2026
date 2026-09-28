# ==================================================================
#  p087-modificar-lista.py
#  Listas en Python - Parte 1 | Ejemplo 2: Modificar elementos de una lista
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Se tiene una lista de calificaciones y se deben corregir algunas:
#   - Cambiar calificaciones en una posicion determinada.
#   - Actualizar las calificaciones en un rango de posiciones.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista fija de calificaciones (califs).
#  Proceso : lista[indice] = valor para un elemento;
#            lista[ini:fin] = [valores] para un rango.
#  Salida  : la lista antes y despues de cada modificacion.
# ==================================================================

califs = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print("\033[2J\033[H", end="", flush=True)
print("Modificar los elementos de una lista")
print("-" * 60)

print(f"\nTodas las calificaciones: {califs}")

print("\nModificar calificaciones en posiciones [0] y [1] con 7 y 7:")
califs[0] = 7
califs[1] = 7
print(f"Resultado: {califs}")

print("\nModificar calificaciones en el rango [2:5] (5 no incluida) con 9, 9, 9:")
califs[2:5] = [9, 9, 9]
print(f"Resultado: {califs}")

print("\n\nGracias por utilizar este programa...")
