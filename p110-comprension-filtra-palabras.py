# ==================================================================
#  p110-comprension-filtra-palabras.py
#  Tarea 5 - Listas | Ejercicio 7: Filtrar palabras con comprension
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Dada una lista de palabras introducidas por el usuario separadas
#  por espacios, usar comprension de listas para crear una nueva lista
#  con las palabras de mas de 4 caracteres convertidas a mayusculas.
#  Imprimir la lista original y la lista filtrada.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : palabras separadas por espacios.
#  Proceso : split() para crear la lista; comprension con filtro
#            len(p) > 4 y transformacion p.upper().
#  Salida  : lista original y lista filtrada.
#  Ejemplo : sol computadora gato programacion python red
#            -> ['COMPUTADORA', 'PROGRAMACION', 'PYTHON']
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Filtrar palabras con comprension")
print("-" * 60)

while True:
    palabras = input("Introduzca palabras separadas por espacios: ").split()
    if palabras:
        break
    print("  Debe introducir al menos una palabra.")

filtradas = [p.upper() for p in palabras if len(p) > 4]

print("\n--- Resultados ---")
print(f"Lista original: {palabras}")
print(f"Lista filtrada (>4 caracteres en mayúsculas): {filtradas}")
