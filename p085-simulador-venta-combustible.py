# ===============================================================
# Examen Práctico Complementario - Computación Aplicada
# Archivo: p085_SimuladorVentaCombustible.py
# Alumno: Josue Julian Ramirez Rosales
# Descripción: Simulador de estación de servicio (gasolinera)
# ===============================================================

# --- Constantes de configuración (int) ---
LIMITE_REGULAR = 100      # litros/mes: menos de esto es "Regular"
LIMITE_PREMIUM = 500      # litros/mes: más de esto es "Flotilla"
MESES_SIMULACION = 12     # meses de la tabla de rendimiento
PASO_KM = 10 ** 2         # km recorridos por mes (100)
ANCHO_LINEA = 38          # ancho de las líneas decorativas

# --- Variables de control del menú (str) ---
opcion = ""

# --- Variables del módulo de venta ---
tipo_combustible = ""     # str
precio = 0.0              # float
litros = 0.0              # float
total = 0.0               # float

# --- Variables del módulo de rendimiento ---
km_inicial = 0            # int
rendimiento = 0.0         # float (km por litro)

# --- Variables del clasificador ---
litros_mensuales = 0.0    # float
categoria = ""            # str

tipo = input("Tipo de combustible (Magna/Premium/Diésel): ")
precio = float(input("Precio por litro: $"))
litros = float(input("Cantidad de litros: "))

if precio <= 0 or litros <= 0:
    print("Error: el precio y los litros deben ser positivos.")
else:
    total = precio * litros
    print("-" * 34)
    print(f"{'Combustible:':<14}{tipo:>20}")
    print(f"{'Precio/litro:':<14}{'$' + f'{precio:.2f}':>20}")
    print(f"{'Litros:':<14}{litros:>20.2f}")
    print(f"{'TOTAL:':<14}{'$' + f'{total:.2f}':>20}")
    print("-" * 34)