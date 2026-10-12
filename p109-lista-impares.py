# ==================================================================
#  p109-lista-impares.py
#  Tarea 5 - Listas | Ejercicio 6: Lista de impares
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Leer un entero n. Llenar una lista con los primeros n numeros
#  impares. Calcular e imprimir:
#   - La suma y el promedio de los numeros.
#   - Los numeros divisibles entre 3 y su suma.
#   - Pedir un elemento a buscar e indicar si esta y en que posicion.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : n (entero > 0) y elemento a buscar (entero).
#  Proceso : comprension 2*i + 1 con range(n); sum() y len();
#            comprension con filtro (x % 3 == 0); operador in e
#            index() para la busqueda.
#  Salida  : lista, suma, promedio, divisibles entre 3 y su suma,
#            resultado de la busqueda.
#  Ejemplo : n = 6 -> [1, 3, 5, 7, 9, 11], suma 36, promedio 6.0,
#            divisibles [3, 9] suma 12; buscar 7 -> indice 3
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Lista de impares")
print("-" * 60)

# Captura validada de n
while True:
    try:
        n = int(input("Introduzca la cantidad de números impares (n): "))
        if n > 0:
            break
        print("  n debe ser mayor que 0.")
    except ValueError:
        print("  Entrada invalida, debe ser un numero entero.")

impares = [2 * i + 1 for i in range(n)]

print("\n--- Generación de Lista ---")
print(f"Lista de los primeros {n} números impares: {impares}")

suma = sum(impares)
print("\n--- Cálculos ---")
print(f"Suma de los números: {suma}")
print(f"Promedio de los números: {suma / len(impares)}")

divisibles = [x for x in impares if x % 3 == 0]
print("\n--- Divisibles entre 3 ---")
print(f"Números divisibles entre 3: {divisibles}")
print(f"Suma de los números divisibles entre 3: {sum(divisibles)}")

print("\n--- Búsqueda ---")
while True:
    try:
        buscado = int(input("Introduzca elemento a buscar: "))
        break
    except ValueError:
        print("  Entrada invalida, debe ser un numero entero.")

if buscado in impares:
    print(f"Resultado: El elemento {buscado} está en la lista "
          f"en la posición (índice) {impares.index(buscado)}.")
else:
    print(f"Resultado: El elemento {buscado} no está en la lista.")
