# ==================================================================
#  p095-registro-estudiantes.py
#  Listas en Python - Parte 2 | Ejemplo 4: Registro de estudiantes
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Registrar a los asistentes de un evento:
#   - Introducir el nombre y la edad de cada persona.
#   - El registro termina cuando se introduce * como nombre.
#   - Mostrar dos informes:
#       * Lista de asistentes mayores de edad (18 anios o mas).
#       * Nombre y edad de la persona de mayor edad (reconocimiento).
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : nombre (str) y edad (int) de cada asistente.
#  Proceso : listas paralelas nombres/edades; for para filtrar los
#            mayores de edad; max() + index() para el de mayor edad.
#  Salida  : informe de mayores de edad y persona de mayor edad.
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Sistema de Registro para Evento")
print("-" * 60)
print("Introduce los nombres y edades de los asistentes (* en nombre para terminar)\n")

# Listas paralelas para almacenar los datos
nombres = []
edades = []

# Ciclo para la captura de datos
while True:
    nombre = input("Nombre del asistente: ").strip()
    if nombre == "*":
        break                               # Termina el ciclo si el nombre es *
    if nombre == "":
        print("El nombre no puede estar vacio.")
        continue
    try:
        edad = int(input(f"Edad de {nombre}: "))
        if edad < 0 or edad > 120:
            print("Por favor, introduce una edad entre 0 y 120.")
            continue
        nombres.append(nombre)              # Agrega el nombre a la lista
        edades.append(edad)                 # Agrega la edad en la misma posicion
    except ValueError:
        print("Por favor, introduce una edad valida (numero entero).")

# --- Generacion de Reportes ---
if not nombres:
    print("\nNo se registraron asistentes.")
else:
    print(f"\nTotal de asistentes registrados: {len(nombres)}")

    # Reporte 1: asistentes mayores de edad
    print("\n--- Asistentes mayores de edad (18+) ---")
    mayores = 0
    for i in range(len(nombres)):
        if edades[i] >= 18:
            print(f"- {nombres[i]} ({edades[i]} anios)")
            mayores += 1
    if mayores == 0:
        print("No hay asistentes mayores de edad.")

    # Reporte 2: persona con mayor edad
    edad_max = max(edades)
    pos_max = edades.index(edad_max)
    print("\n--- Reconocimiento al asistente de mayor edad ---")
    print(f"{nombres[pos_max]} con {edad_max} anios.")

print("\n\nGracias por utilizar este programa...")
