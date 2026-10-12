# ==================================================================
#  p107-listas-aleatorios-suma.py
#  Tarea 5 - Listas | Ejercicio 4: Suma de impares en listas aleatorias
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Generar 2 listas de 10 numeros aleatorios cada una. Crear una
#  tercera lista cuyo elemento sea la suma de los correspondientes de
#  A y B solo si AMBOS son impares; de lo contrario sera 0.
#  Imprimir las 3 listas.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : ninguna (numeros aleatorios del 1 al 20).
#  Proceso : random.randint() en comprensiones para A y B;
#            comprension con expresion condicional:
#            A[i] + B[i] si ambos son impares, si no 0.
#  Salida  : listas A, B y C.
#  Ejemplo : A[2]=3, B[2]=9 -> 12 ; A[1]=8 (par), B[1]=1 -> 0
# ==================================================================

import random

print("\033[2J\033[H", end="", flush=True)
print("Suma de impares en listas aleatorias")
print("-" * 60)

TAMANIO = 10

lista_a = [random.randint(1, 20) for _ in range(TAMANIO)]
lista_b = [random.randint(1, 20) for _ in range(TAMANIO)]

# Suma solo si ambos elementos son impares
lista_c = [lista_a[i] + lista_b[i]
           if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0 else 0
           for i in range(TAMANIO)]

print("--- Listas Generadas ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")

print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
print(f"Lista C: {lista_c}")
