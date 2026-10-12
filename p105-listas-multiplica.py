# ==================================================================
#  p105-listas-multiplica.py
#  Tarea 5 - Listas | Ejercicio 2: Multiplicar listas
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Leer dos listas, cada una con 5 elementos numericos. Crear una
#  tercera lista multiplicando los elementos correspondientes de las
#  dos listas. Imprimir las tres listas.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : 5 numeros para la lista A y 5 para la lista B (en una
#            sola linea, separados por espacios).
#  Proceso : split() para separar, conversion a numero con validacion;
#            comprension con range(len()) para C[i] = A[i] * B[i].
#  Salida  : listas A, B y C.
#  Ejemplo : A = [2, 4, 6, 8, 10], B = [5, 1, 3, 7, 9]
#            -> C = [10, 4, 18, 56, 90]
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Multiplicar listas")
print("-" * 60)

TAMANIO = 5
listas = []

# Captura de las dos listas
for nombre in ["A", "B"]:
    while True:
        datos = input(f"Introduzca {TAMANIO} números para la Lista {nombre}: ").split()
        if len(datos) != TAMANIO:
            print(f"  Debe introducir exactamente {TAMANIO} numeros.")
            continue
        try:
            numeros = []
            for d in datos:
                num = float(d)
                numeros.append(int(num) if num.is_integer() else num)
            break
        except ValueError:
            print("  Entrada invalida, solo se permiten numeros.")
    listas.append(numeros)

lista_a, lista_b = listas

# Producto elemento a elemento
lista_c = [lista_a[i] * lista_b[i] for i in range(TAMANIO)]

print("\n--- Resultados ---")
print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Lista C (A * B): {lista_c}")
