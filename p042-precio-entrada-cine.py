# p042-precio-entrada-cine.py
# Determinar el precio de una entrada de cine segun la edad del cliente.
print("\033[2J\033[H", end="", flush=True)
print('--- Taquilla del Cine ---')
# Pedir la edad del cliente
edad = int(input('Edad del cliente: '))
# La estructura if/elif evalua cada rango de edad
if edad < 5:
    precio = 0
elif edad <= 12:
    precio = 5
elif edad <= 64:
    precio = 10
else:
    precio = 7
print(f' El precio de la entrada es ${precio}.')
