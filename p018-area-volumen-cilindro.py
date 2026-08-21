# p018-area-volumen-cilindro
# Calcular el área y el volumen de un cilindro
import math

print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario el radio y la altura del cilindro
radio = float(input("Ingresa el radio (R) del cilindro: "))
altura = float(input("Ingresa la altura (h) del cilindro: "))
# Calcular el área y el volumen del cilindro
area = 2 * math.pi * (radio + altura)
volumen = math.pi * radio ** 2 * altura
# Formatear la salida 
salida = ('Resumen del cálculo\n'
f'Radio: {radio:.2f}\n'
f'Altura: {altura:.2f}\n'
f'El área del cilindro es {area:.4f}\n'
f'El volumen del cilindro es {volumen:.4f}\n')
# Mostrar la salida con formato
print(salida)
