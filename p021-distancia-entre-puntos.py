# p021-distancia-entre-puntos
# Calcular la distancia entre dos puntos en un plano cartesiano
import math

print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario las coordenadas del punto A y del punto B
x1 = float(input("Ingresa la coordenada x del punto A: "))
y1 = float(input("Ingresa la coordenada y del punto A: "))
x2 = float(input("Ingresa la coordenada x del punto B: "))
y2 = float(input("Ingresa la coordenada y del punto B: "))

# Calcular la distancia entre los dos puntos
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# Formatear la salida 
salida = ('Resumen del cálculo\n'
f'Punto A: ({x1:.2f}, {y1:.2f})\n'
f'Punto B: ({x2:.2f}, {y2:.2f})\n'
f'La distancia entre los dos puntos es {distancia:.4f}\n')
# Mostrar la salida con formato
print(salida)
