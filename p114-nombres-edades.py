# ==================================================================
#  p114-nombres-edades.py
#  Diccionarios en Python - Parte 1 | Ejemplo 3: Nombres y edades
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Programa interactivo que funcione como un pequeno censo:
#   - Pedir un nombre y una edad repetidamente, en un bucle.
#   - Guardar cada par nombre: edad en un diccionario.
#   - Terminar cuando el usuario ingrese un nombre vacio (Enter).
#   - Mostrar el diccionario completo y el numero de personas, un
#     listado formateado y la suma y el promedio de las edades.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : pares nombre / edad (entero, 0 a 120).
#  Proceso : ciclo while True con break en nombre vacio; asignacion
#            datos[nombre] = edad; validacion con try/except; for
#            sobre .items() acumulando la suma.
#  Salida  : diccionario, total de personas, listado, suma y
#            promedio.
#  Ejemplo : Ana 20, Luis 30, Eva 25 -> suma 75, promedio 25.00
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Gestion de nombres y edades usando diccionarios")
print("-" * 60)

datos = {}
print("Introduce nombres y edades (nombre vacio para terminar)\n")

while True:
    nombre = input("Dame el nombre ? ").strip()
    if nombre == '':
        break
    while True:
        try:
            edad = int(input("Edad ? "))
            if 0 <= edad <= 120:
                break
            print("La edad debe estar entre 0 y 120. Intente de nuevo.")
        except ValueError:
            print("Entrada no valida. Ingrese un numero entero.")
    datos[nombre] = edad

print(f"\nEl diccionario de datos creado:\n{len(datos)} - {datos}")
print("\nListado y promedio de edades:\n")

s = 0
for n, e in datos.items():
    print(f"{n:<20} - {e:3}")
    s += e

p = s / len(datos) if datos else 0
print(f"\nSuma: {s} y promedio: {p:.2f}")
