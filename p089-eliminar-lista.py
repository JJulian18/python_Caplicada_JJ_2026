# ==================================================================
#  p089-eliminar-lista.py
#  Listas en Python - Parte 1 | Ejemplo 4: Eliminar elementos de una lista
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Se tiene una lista de mediciones con valores erroneos. Se debe:
#   - Eliminar un valor anomalo especifico.
#   - Quitar el valor incorrecto de una posicion especifica y
#     guardarlo para un reporte.
#   - Eliminar el ultimo valor (medicion incompleta).
#   - Borrar todos los datos para empezar un nuevo analisis.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista fija de mediciones con anomalias (nums).
#  Proceso : remove(valor) elimina la primera ocurrencia;
#            pop(indice) elimina y devuelve un elemento;
#            pop() elimina y devuelve el ultimo; clear() vacia la lista.
#  Salida  : la lista y los valores removidos tras cada operacion.
# ==================================================================

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]

print("\033[2J\033[H", end="", flush=True)
print("Eliminar elementos de una lista")
print("-" * 60)

print(f"\nDatos originales con anomalias: {nums}\n")

print("Eliminar el valor 99 (remove):")
nums.remove(99)
print(f"Resultado : {nums}\n")

# Tras quitar el 99, el valor anomalo 88 quedo en la posicion 7
print("Eliminar el elemento en la posicion 7 y guardarlo (pop):")
num_removido = nums.pop(7)
print(f"Resultado : Removido ({num_removido}), {nums}\n")

print("Eliminar el ultimo elemento (pop sin indice):")
ultimo_num = nums.pop()
print(f"Resultado : Removido ({ultimo_num}), {nums}\n")

print("Eliminar todos los elementos de la lista (clear):")
nums.clear()
print(f"Resultado : {nums}")

print("\n\nGracias por utilizar este programa...")
