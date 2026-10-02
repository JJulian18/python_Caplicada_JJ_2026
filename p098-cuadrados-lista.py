# ==================================================================
#  p098-cuadrados-lista.py
#  Listas en Python - Parte 3 | Ejemplo 1: Cuadrados de numeros
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Generar cuadrados:
#   - Dado un limite n, crear una lista con los numeros del 1 al n.
#   - Generar otra lista con el cuadrado de cada numero usando una
#     comprension de listas.
#   - Mostrar la lista original y la lista transformada.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : n (int) - limite superior, debe ser mayor que 0.
#  Proceso : list(range(1, n + 1)) para la lista original;
#            [numero ** 2 for numero in numeros] para transformarla.
#  Salida  : lista de numeros y lista de cuadrados.
#  Ejemplo : n = 5 -> [1, 2, 3, 4, 5] -> [1, 4, 9, 16, 25]
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Cuadrados de numeros")
print("-" * 60)

# Validar que el limite sea un entero positivo
while True:
    try:
        n = int(input("Hasta que numero? "))
        if n > 0:
            break
        print("Error: el numero debe ser mayor que 0.")
    except ValueError:
        print("Entrada no valida. Por favor, introduce un numero entero.")

numeros = list(range(1, n + 1))                       # lista original
cuadrados = [numero ** 2 for numero in numeros]       # comprension

print(f"\nNumeros  : {numeros}")
print(f"Cuadrados: {cuadrados}")
