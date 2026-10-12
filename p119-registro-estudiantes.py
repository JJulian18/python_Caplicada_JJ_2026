# ==================================================================
#  p119-registro-estudiantes.py
#  Diccionarios en Python - Parte 2 | Ejemplo 2: Registro estudiantes
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Registrar estudiantes en un grupo:
#   - Agregar multiples estudiantes capturando nombre, edad,
#     carrera y promedio.
#   - Cada estudiante se almacena como un diccionario dentro de
#     una lista general (grupo).
#   - Al ingresar un nombre vacio termina la captura y se imprime
#     un reporte completo del grupo.
#   - Calcular la suma de los promedios y el promedio general.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : nombre, edad (entero > 0), carrera y promedio (0-10);
#            nombre vacio para terminar.
#  Proceso : while True con break; diccionario datos agregado con
#            append(); for anidado sobre .values() y .items();
#            acumulador s += est['promedio']; p = s / len(grupo).
#  Salida  : grupo completo, tabla, registros, suma y promedio.
#  Ejemplo : Carlos 9, Rocio 10 + Ana 8 -> suma 27.0, promedio 9.00
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Registro de Estudiantes")
print("-" * 60)

grupo = [
    {'nombre': 'Carlos', 'edad': 45, 'carrera': 'sistemas', 'promedio': 9},
    {'nombre': 'Rocio', 'edad': 35, 'carrera': 'sistemas', 'promedio': 10}
]

print(f"\nGrupo de estudiantes inicial:\n{'-' * 60}\n{grupo} - {len(grupo)}")

print("\nCaptura de nuevos estudiantes (nombre vacio para terminar)")
print("-" * 60)
while True:
    print("Datos Estudiante:")
    datos = {}
    nombre = input("Nombre ? ").strip()
    if nombre == '':
        break
    datos['nombre'] = nombre
    while True:
        try:
            edad = int(input("Edad ? "))
            if edad > 0:
                break
            print("Error: la edad debe ser un entero positivo.")
        except ValueError:
            print("Error: ingrese un numero entero (ej. 20).")
    datos['edad'] = edad
    datos['carrera'] = input("Carrera ? ").strip()
    while True:
        try:
            promedio = float(input("Promedio ? "))
            if 0 <= promedio <= 10:
                break
            print("Error: el promedio debe estar entre 0 y 10.")
        except ValueError:
            print("Error: ingrese un numero (ej. 8.5).")
    datos['promedio'] = promedio
    grupo.append(datos)
    print("")

print(f"\nGrupo de estudiantes completo:\n{'-' * 60}\n{grupo} - {len(grupo)}")

print("\nDatos en forma de Tabla:")
print("-" * 60)
for k in grupo[0].keys():
    print(f"{k:<13}", end="")
print("")
for alumno in grupo:
    for v in alumno.values():
        print(f"{v:<13}", end="")
    print("")

print("\nDatos en forma de Registro y Cálculo de Promedios:")
print("-" * 60)
s = 0
for est in grupo:
    s += est['promedio']
    for k, v in est.items():
        print(f"{k:<10} : {v}")
    print("")

print("\nCálculo de Promedios:")
print("-" * 60)
p = s / len(grupo)
print(f"La suma es {s}")
print(f"El promedio es {p:.2f}")
