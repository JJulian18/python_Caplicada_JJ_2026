# ==================================================================
#  p116-conversion-divisas.py
#  Diccionarios en Python - Parte 1 | Ejemplo 5: Conversor divisas
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Implementar un conversor de divisas a pesos mexicanos (MXN):
#   - Definir un diccionario conversiones con las tasas de cambio
#     (USD, EUR, GBP, JPY, CAD) a MXN.
#   - Iterar sobre las llaves para mostrar las monedas disponibles.
#   - Solicitar la moneda y validar que exista en el diccionario.
#   - Solicitar la cantidad a convertir (numero positivo).
#   - Multiplicar la cantidad por la tasa de cambio y mostrarla.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : moneda (llave del diccionario) y cantidad (real > 0).
#  Proceso : for sobre las llaves; operador in para validar;
#            try/except ValueError para la cantidad; acceso
#            conversiones[moneda].
#  Salida  : cantidad equivalente en MXN.
#  Ejemplo : 100 USD -> 2,050.00 MXN ; 1000 JPY -> 190.00 MXN
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Conversor de monedas a pesos mexicanos (MXN)")
print("-" * 60)

conversiones = {
    'USD': 20.50,
    'EUR': 22.30,
    'GBP': 25.80,
    'JPY': 0.19,
    'CAD': 16.20
}

print("Opciones de monedas:")
for moneda in conversiones:
    print(f" - {moneda}  (1 {moneda} = {conversiones[moneda]:.2f} MXN)")

while True:
    moneda = input("\nIngrese la moneda a convertir: ").strip().upper()
    if moneda in conversiones:
        break
    else:
        print("Moneda no valida. Intente de nuevo.")

while True:
    try:
        cantidad = float(input(f"Ingrese la cantidad en {moneda}: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser un numero positivo. Intente de nuevo.")
    except ValueError:
        print("Entrada no valida. Por favor, ingrese un numero (ej. 150.50).")

resultado = cantidad * conversiones[moneda]

print(f"\n{cantidad:,.2f} {moneda} son {resultado:,.2f} MXN")
