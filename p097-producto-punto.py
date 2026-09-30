# ==================================================================
#  p097-producto-punto.py
#  Listas en Python - Parte 2 | Ejemplo 6: Producto punto
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Dados dos vectores representados como listas:
#   - Verificar que tengan la misma longitud; si no, mostrar error.
#   - Calcular el producto punto: multiplicar los elementos de la
#     misma posicion y sumar todos esos productos.
#   - Mostrar el resultado final.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : vectores fijos vector_a y vector_b.
#  Proceso : len() para validar; for con acumulador para sumar
#            vector_a[i] * vector_b[i].
#  Salida  : desglose del calculo y el producto punto.
#  Ejemplo : (1*4) + (3*-2) + (-5*-1) = 4 - 6 + 5 = 3
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("--- Calculo del Producto Punto ---")
print("-" * 60)

# Vectores representados como listas
vector_a = [1, 3, -5]
vector_b = [4, -2, -1]
producto_punto = 0

print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}\n")

# 1. Verificar que los vectores tengan la misma longitud
if len(vector_a) == len(vector_b):
    # 2. Multiplicar elementos y sumar los resultados
    terminos = []
    for i in range(len(vector_a)):
        producto = vector_a[i] * vector_b[i]
        producto_punto += producto
        terminos.append(f"({vector_a[i]}*{vector_b[i]})")

    # 3. Mostrar el resultado
    print("Calculo: " + " + ".join(terminos) + f" = {producto_punto}")
    print(f"El producto punto de los vectores es: {producto_punto}")
else:
    print("Error: Los vectores deben tener la misma longitud para calcular el producto punto.")

print("\n\nGracias por utilizar este programa...")
