# ==================================================================
#  p108-ciudades.py
#  Tarea 5 - Listas | Ejercicio 5: Ciudades
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Leer nombres de ciudades en una lista hasta que el usuario
#  introduzca el caracter $. Imprimir:
#   - Cuantos elementos tiene la lista.
#   - La lista completa.
#   - La lista ordenada en orden descendente.
#   - Cuantas ciudades inician con consonante y sus nombres.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : nombres de ciudades ($ para detener).
#  Proceso : while True + append(); len(); sorted(reverse=True);
#            comprension con filtro (primera letra no es vocal).
#  Salida  : total, lista original, lista descendente y ciudades que
#            inician con consonante.
#  Ejemplo : Aguascalientes, Monterrey, Oaxaca, Saltillo
#            -> consonante: ['Monterrey', 'Saltillo']
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Ciudades")
print("-" * 60)

VOCALES = "AEIOUÁÉÍÓÚÜ"
ciudades = []

# Captura de ciudades hasta introducir $
while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ").strip()
    if ciudad == "$":
        break
    if ciudad == "" or not ciudad[0].isalpha():
        print("  Nombre invalido, debe iniciar con una letra.")
        continue
    ciudades.append(ciudad)

print("\n--- Resultados ---")
if not ciudades:
    print("No se introdujeron ciudades.")
else:
    descendente = sorted(ciudades, reverse=True)
    consonantes = [c for c in ciudades if c[0].upper() not in VOCALES]

    print(f"Total de ciudades introducidas: {len(ciudades)}")
    print(f"Lista original: {ciudades}")
    print(f"Lista ordenada descendente: {descendente}")
    print(f"Ciudades que inician con consonante: {len(consonantes)}")
    print(f"Lista de ciudades con consonante inicial: {consonantes}")
