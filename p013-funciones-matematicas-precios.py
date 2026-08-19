# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matemáticas para redondeo y manejo de precios
import math

print("\033[2J\033[H", end="", flush=True)

# Precio con decimales
precio = float(input("Ingresa un precio con decimales: "))
# Diferentes métodos de redondeo
arriba = math.ceil(precio)
abajo = math.floor(precio)
truncado = math.trunc(precio)
redondeo = round(precio)
un_decimal = round(precio, 1)
# Mostrar resultados con formato

print("\033[2J\033[H", end="", flush=True)

print(f"Precio original. : ${precio}")
print(f"Redondeo arriba (ceil): ${arriba}")
print(f"Redondeo abajo (floor): ${abajo}")
print(f"Truncado (trunc) : ${truncado}")
print(f"Redondeo normal : ${redondeo}")
print(f"Redondeo 1 decimal : ${un_decimal}")