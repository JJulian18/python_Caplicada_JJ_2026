# ==================================================================
#  p090-iterar-lista.py
#  Listas en Python - Parte 1 | Ejemplo 5: Iterar por los elementos de una lista
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Dada una lista de numeros, realizar las siguientes operaciones:
#   - Imprimir cada numero de la lista.
#   - Imprimirlos otra vez, accediendo por su indice.
#   - Crear una nueva secuencia donde a cada numero se le suma 2.
#   - Generar otra secuencia donde a cada numero se le suma 10,
#     usando su indice.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista fija de numeros (nums).
#  Proceso : for directo sobre elementos; for con range(len());
#            append() para construir la nueva secuencia (+2);
#            asignacion por indice para modificar la lista (+10);
#            enumerate() para mostrar posicion y valor.
#  Salida  : cada secuencia impresa en una linea.
# ==================================================================

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print("\033[2J\033[H", end="", flush=True)
print("Iterar por los elementos de una lista")
print("-" * 60)

print(f"\nNumeros a procesar: {nums}\n")

print("1. Iteracion por elemento:")
for n in nums:
    print(n, end=" ")

print("\n\n2. Iteracion por indice:")
for i in range(len(nums)):
    print(nums[i], end=" ")

print("\n\n3. Iteracion por elemento para sumar 2 (nueva secuencia):")
nums_mas_2 = []
for n in nums:
    nums_mas_2.append(n + 2)
print(nums_mas_2)

print("\n4. Iteracion por indice para sumar 10 (modifica la lista original):")
for i in range(len(nums)):
    nums[i] += 10
    print(nums[i], end=" ")

print("\n\n5. Iteracion con enumerate:")
print("Pos\tValor")
for i, n in enumerate(nums):
    print(f"{i}\t{n}")

print("\n\nGracias por utilizar este programa...")
