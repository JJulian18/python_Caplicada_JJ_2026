# ==================================================================
#  p102-aplanar-matriz.py
#  Listas en Python - Parte 3 | Ejemplo 5: Aplanar una matriz
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Dada una matriz representada por una lista de listas:
#   - Recorrer cada fila y cada elemento.
#   - Crear una sola lista con todos los valores.
#   - Crear ademas una lista con unicamente los valores positivos.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : matriz fija 3x3.
#  Proceso : comprension anidada
#            [numero for fila in matriz for numero in fila]
#            y la misma con filtro if numero > 0.
#  Salida  : matriz, lista plana y valores positivos.
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Aplanar una matriz")
print("-" * 60)

matriz = [[4, -2, 8], [0, 5, -1], [7, 3, -6]]

valores = [numero for fila in matriz for numero in fila]

positivos = [numero for fila in matriz
             for numero in fila if numero > 0]

print("Matriz:")
for fila in matriz:
    print("   " + " ".join(f"{n:>3}" for n in fila))

print(f"\nLista plana      : {valores}")
print(f"Valores positivos: {positivos}")
