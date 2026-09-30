# ==================================================================
#  p093-consolidar-ventas.py
#  Listas en Python - Parte 2 | Ejemplo 2: Consolidar ventas
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Una empresa tiene dos sucursales y necesita consolidar sus ventas:
#   - Leer las ventas de cada dia para ambas sucursales y guardarlas
#     en dos listas separadas.
#   - Calcular las ventas totales por dia en una tercera lista.
#   - Mostrar las ventas de ambas sucursales y el consolidado.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : numero de dias (int) y la venta de cada dia (int) por
#            sucursal.
#  Proceso : for + append() para llenar las listas; suma elemento a
#            elemento (misma posicion) para el consolidado.
#  Salida  : tabla por dia con ambas sucursales y el consolidado.
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Consolidar ventas de dos sucursales")
print("-" * 60)


def leer_entero(mensaje):
    """Pide un entero >= 0 y repite hasta que sea valido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: el valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Error: introduce un numero entero valido.")


elementos = leer_entero("Cuantas ventas diarias se registraran? ")

# Inicializar listas
ventas_suc1 = []
ventas_suc2 = []
ventas_consolidadas = []

# Leer datos de la Sucursal 1
print("\nRegistrando ventas de la Sucursal 1:")
for i in range(elementos):
    ventas_suc1.append(leer_entero(f"Venta del dia {i + 1}: "))

# Leer datos de la Sucursal 2
print("\nRegistrando ventas de la Sucursal 2:")
for i in range(elementos):
    ventas_suc2.append(leer_entero(f"Venta del dia {i + 1}: "))

# Consolidar: sumar las ventas de la misma posicion (mismo dia)
for i in range(elementos):
    ventas_consolidadas.append(ventas_suc1[i] + ventas_suc2[i])

print("\n--- Reporte de ventas ---")
print(f"Sucursal 1   : {ventas_suc1}")
print(f"Sucursal 2   : {ventas_suc2}")
print(f"Consolidado  : {ventas_consolidadas}")

print(f"\n{'Dia':>4} {'Suc. 1':>12} {'Suc. 2':>12} {'Total':>12}")
for i in range(elementos):
    print(f"{i + 1:>4} {ventas_suc1[i]:>12,} {ventas_suc2[i]:>12,} {ventas_consolidadas[i]:>12,}")
print(f"{'Suma':>4} {sum(ventas_suc1):>12,} {sum(ventas_suc2):>12,} {sum(ventas_consolidadas):>12,}")

print("\n\nGracias por utilizar este programa...")
