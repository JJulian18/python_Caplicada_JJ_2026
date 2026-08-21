# p017-convertir-temperatura
# Convertir una temperatura de grados Celsius a grados Fahrenheit
print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario la temperatura en Celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
# Calcular la temperatura equivalente en Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32
# Formatear la salida 
salida = ('Resumen del cálculo\n'
f'Temperatura en Celsius: {celsius:.2f}°C\n'
f'Temperatura en Fahrenheit: {fahrenheit:.2f}°F\n')
# Mostrar la salida con formato
print(salida)
