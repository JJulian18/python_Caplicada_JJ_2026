# ==================================================================
#  p111-comprension-pares-cuadrados.py
#  Tarea 5 - Listas | Ejercicio 8: Cuadrados de pares con comprension
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Generar una lista de enteros del 1 al n (n ingresado por el
#  usuario). Con comprension de listas obtener una nueva lista con los
#  cuadrados unicamente de los numeros pares. Imprimir la lista del
#  rango completo, la lista de cuadrados y la suma de los cuadrados.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : limite n (entero > 0).
#  Proceso : list(range(1, n + 1)); comprension con filtro x % 2 == 0
#            y transformacion x ** 2; sum().
#  Salida  : lista original, cuadrados de pares y su suma.
#  Ejemplo : n = 10 -> [4, 16, 36, 64, 100], suma 220
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Cuadrados de pares con comprension")
print("-" * 60)

while True:
    try:
        n = int(input("Introduzca el límite n: "))
        if n > 0:
            break
        print("  n debe ser mayor que 0.")
    except ValueError:
        print("  Entrada invalida, debe ser un numero entero.")

numeros = list(range(1, n + 1))
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]

print("\n--- Resultados ---")
print(f"Lista original (1 a {n}): {numeros}")
print(f"Cuadrados de números pares: {cuadrados}")
print(f"Suma de cuadrados: {sum(cuadrados)}")
