# ==================================================================
#  p117-punto-de-venta.py
#  Diccionarios en Python - Parte 1 | Ejemplo 6: Punto de venta
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Sistema simple de punto de venta (POS) para un puesto de comida:
#   - Definir un diccionario menu con productos y precios.
#   - Mostrar el menu iterando sobre el diccionario.
#   - Preguntar en un bucle que desea ordenar:
#       * si el producto no esta en el menu, informarlo;
#       * si existe, solicitar la cantidad (entero positivo,
#         validado con try/except ValueError).
#   - Almacenar la orden en otro diccionario (el carrito).
#   - Al escribir 'fin', mostrar un recibo con el subtotal por
#     producto y el total general.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : nombre del producto y cantidad, hasta escribir 'fin'.
#  Proceso : for sobre .items() para el menu; operador in / not in;
#            orden.get(producto, 0) + cantidad para acumular;
#            for sobre la orden calculando subtotales y total.
#  Salida  : recibo con cantidad, producto, subtotal y total.
#  Ejemplo : 3 taco + 2 refresco -> $55.50 + $40.00 = $95.50
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Simulacion de un punto de venta usando diccionarios")
print("-" * 60)

menu = {
    'taco': 18.50,
    'burrito': 45.00,
    'quesadilla': 35.00,
    'refresco': 20.00,
    'agua': 15.00
}

print("--- Bienvenido a 'El Taco Feroz' ---")
print("Este es nuestro menú:")
for item, precio in menu.items():
    print(f" - {item:<12} : ${precio:>7,.2f}")
print("-" * 35)

orden = {}
total_general = 0

while True:
    producto = input("\n¿Qué desea ordenar? (escriba 'fin' para terminar): ").strip().lower()
    if producto == 'fin':
        break
    if producto not in menu:
        print("Error: Ese producto no está en el menú. Intente de nuevo.")
        continue
    try:
        cantidad = int(input(f"¿Cuántos '{producto}' desea?: "))
        if cantidad <= 0:
            print("Error: La cantidad debe ser un número positivo.")
            continue
    except ValueError:
        print("Error: Debe ingresar un número entero (ej. 2).")
        continue

    orden[producto] = orden.get(producto, 0) + cantidad
    print(f"Agregados {cantidad} {producto}(s) a su orden.")

print("\n--- SU RECIBO ---")
if not orden:
    print("No se ordenó ningún producto.")
else:
    for producto, cantidad in orden.items():
        precio_unitario = menu[producto]
        subtotal = precio_unitario * cantidad
        print(f" {cantidad:>3} x {producto:<12} : ${subtotal:>8,.2f}")
        total_general += subtotal

    print("-" * 35)
    print(f"TOTAL A PAGAR: ${total_general:,.2f}")
    print("¡Gracias por su compra!")
