# p016-tercer-angulo
# Determinar el tercer ángulo de un triángulo
print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario las medidas de dos ángulos del triángulo
angulo1 = float(input("Ingresa la medida del primer ángulo: "))
angulo2 = float(input("Ingresa la medida del segundo ángulo: "))
# Calcular el ángulo faltante
angulo3 = 180 - (angulo1 + angulo2)
# Formatear la salida
salida = ('Resumen del cálculo\n'
f'Ángulo 1: {angulo1:.2f}°\n'
f'Ángulo 2: {angulo2:.2f}°\n'
f'El tercer ángulo del triángulo es {angulo3:.2f}°\n')
# Mostrar la salida formateada
print(salida)
