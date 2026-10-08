# ==================================================================
#  p115-conversor-unidades.py
#  Diccionarios en Python - Parte 1 | Ejemplo 4: Conversion de
#  medidas
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Crear un conversor de unidades de longitud:
#   - Definir un diccionario conversiones con los factores para
#     convertir 'km', 'm', 'cm' y 'mm' a metros.
#   - Solicitar al usuario una longitud (numero).
#   - Pedir la unidad de medida y volver a pedirla si no es una
#     llave valida.
#   - Usar el factor del diccionario para calcular los metros.
#   - Mostrar el resultado formateado.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : longitud (real) y unidad (km, m, cm, mm).
#  Proceso : validacion con try/except; operador in para verificar
#            que la unidad sea llave; acceso conversiones[unidad].
#  Salida  : longitud equivalente en metros.
#  Ejemplo : 2.5 km -> 2,500.00 metros ; 350 cm -> 3.50 metros
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Conversor de unidades de longitud usando diccionarios")
print("-" * 60)

conversiones = {
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

while True:
    try:
        longitud = float(input("Dame la longitud ? "))
        break
    except ValueError:
        print("Entrada no valida. Ingrese un numero (ej. 2.5).")

while True:
    unidad = input("Unidad (km, m, cm, mm) ? ").strip().lower()
    if unidad in conversiones:
        break
    else:
        print("Unidad no valida. Intente de nuevo.")

resultado = longitud * conversiones[unidad]

print(f"\n{longitud:,.2f} {unidad} son {resultado:,.2f} metros")
