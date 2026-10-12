# ==================================================================
#  p120-reporte-ventas.py
#  Diccionarios en Python - Parte 2 | Ejemplo 3: Cliente y productos
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Generar un reporte de ventas de los productos de cada cliente:
#   - Registrar n transacciones de compra; para cada una pedir
#     cliente, producto, cantidad y precio. Cada compra es un
#     diccionario almacenado en una lista de compras.
#   - Procesar la lista para calcular la cantidad total de
#     productos y el subtotal gastado por cada cliente.
#   - Imprimir el resumen de totales por cliente.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : n (entero > 0) y, por compra: cliente, producto,
#            cantidad (entero > 0) y precio (real > 0).
#  Proceso : lista de diccionarios (compras); diccionario de
#            diccionarios (clientes) con "cantidad" y "subtotal";
#            operador not in para crear la entrada del cliente;
#            acumuladores += por cliente.
#  Salida  : lista de compras, totales por cliente y estructura.
#  Ejemplo : Ana 2 x 10, Luis 1 x 50, Ana 3 x 5
#            -> Ana: 5 productos, $35.00 ; Luis: 1 producto, $50.00
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Reporte de Ventas")
print("-" * 60)


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: debe ser un entero positivo.")
        except ValueError:
            print("Error: ingrese un numero entero (ej. 3).")


def pedir_real(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Error: debe ser un numero positivo.")
        except ValueError:
            print("Error: ingrese un numero (ej. 12.50).")


print("\n--- Registro de Transacciones ---")
n = pedir_entero("Número de compras a registrar: ")

compras = []
for i in range(1, n + 1):
    print(f"\n------ Compra {i} ------")
    compra = {
        "cliente": input("Nombre Cliente  : ").strip().title(),
        "producto": input("Nombre Producto : ").strip(),
        "cantidad": pedir_entero("Cantidad        : "),
        "precio": pedir_real("Precio          : ")
    }
    compras.append(compra)

print("\n--- Lista de Compras Registradas ---\n", compras)

clientes = {}  # Diccionario de diccionarios
for compra in compras:
    cliente = compra["cliente"]
    if cliente not in clientes:
        clientes[cliente] = {"cantidad": 0, "subtotal": 0}
    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

print("\n--- Reporte de Totales por Cliente ---\n")
for cliente, datos in clientes.items():
    print(f"Cliente                     : {cliente}")
    print(f"Cantidad Total de Productos : {datos['cantidad']}")
    print(f"Subtotal a Pagar            : ${datos['subtotal']:,.2f}")
    print()

print("\n--- Diccionario de Clientes (Estructura Interna) ---\n", clientes)
