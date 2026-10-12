# ==================================================================
#  p104-procesar-notas.py
#  Tarea 5 - Listas | Ejercicio 1: Procesar notas
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Leer un numero indeterminado de notas entre 0 y 100, deteniendose
#  cuando el usuario introduzca un 0. Validar el rango [0,100].
#  Calcular e imprimir:
#   - Cuantas notas se introdujeron.
#   - La lista de notas completa.
#   - La suma y el promedio de las notas.
#   - La nota maxima y la nota minima.
#   - Cuantas y cuales notas son menores al promedio.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : notas enteras (0 para detener).
#  Proceso : while True + append() para llenar la lista; len(), sum(),
#            max(), min(); comprension con filtro (nota < promedio).
#  Salida  : total, lista, suma, promedio, maxima, minima y notas
#            menores al promedio.
#  Ejemplo : 85 92 78 101(invalida) 65 0 -> suma 320, promedio 80.0,
#            menores al promedio [78, 65]
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Procesar notas")
print("-" * 60)

notas = []

# Captura de notas hasta que se introduzca 0
while True:
    try:
        nota = int(input("Introduzca nota (0 para detener): "))
    except ValueError:
        print("  Entrada invalida, debe ser un numero entero.")
        continue
    if nota == 0:
        break
    if nota < 0 or nota > 100:
        print("  Entrada invalida, debe ser 0-100.")
        continue
    notas.append(nota)

print("\n--- Resultados ---")
if not notas:
    print("No se introdujeron notas.")
else:
    total = len(notas)
    suma = sum(notas)
    promedio = suma / total
    menores = [n for n in notas if n < promedio]

    print(f"Total de notas introducidas: {total}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma}")
    print(f"Promedio de notas: {round(promedio, 2)}")
    print(f"Nota máxima: {max(notas)}")
    print(f"Nota mínima: {min(notas)}")
    print(f"Notas menores al promedio ({round(promedio, 2)}): {len(menores)}")
    print(f"Lista de notas menores al promedio: {menores}")
