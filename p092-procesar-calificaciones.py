# ==================================================================
#  p092-procesar-calificaciones.py
#  Listas en Python - Parte 2 | Ejemplo 1: Procesar calificaciones
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Procesar las calificaciones finales de una clase:
#   - Ingresar calificaciones (entre 0 y 10) una por una hasta que
#     se ingrese 99.
#   - Mostrar un resumen estadistico: la lista de calificaciones,
#     la suma, el promedio, la calificacion mas alta, la mas baja
#     y cuantos alumnos superaron el promedio.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : calificaciones (float) hasta capturar 99.
#  Proceso : append() para guardar; acumulador para la suma;
#            max() y min() para los extremos; for para contar los
#            que superan el promedio.
#  Salida  : resumen estadistico impreso en pantalla.
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Procesador de calificaciones de un curso")
print("-" * 60)
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar):\n")

calificaciones = []          # list  - calificaciones validas
suma = 0.0                   # float - acumulador de calificaciones

while True:
    try:
        n = float(input("Calificacion > "))
        if n == 99:
            break
        if 0 <= n <= 10:
            calificaciones.append(n)
            suma += n
        else:
            print("Error: la calificacion debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no valida. Por favor, introduce un numero.")

if not calificaciones:
    print("\nNo se ingresaron calificaciones.")
else:
    promedio = suma / len(calificaciones)
    mas_alta = max(calificaciones)
    mas_baja = min(calificaciones)

    # Contar cuantos alumnos superaron el promedio
    sobre_promedio = 0
    for c in calificaciones:
        if c > promedio:
            sobre_promedio += 1

    print("\n--- Resumen estadistico ---")
    print(f"Calificaciones        : {calificaciones}")
    print(f"Numero de alumnos     : {len(calificaciones)}")
    print(f"Suma                  : {suma:.2f}")
    print(f"Promedio              : {promedio:.2f}")
    print(f"Calificacion mas alta : {mas_alta}")
    print(f"Calificacion mas baja : {mas_baja}")
    print(f"Superaron el promedio : {sobre_promedio}")

print("\n\nGracias por utilizar este programa...")
