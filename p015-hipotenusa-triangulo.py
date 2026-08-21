# p015-hipotenusa-triangulo
# Calcular la longitud de la hipotenusa de un triángulo rectángulo
import math

print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario la longitud de los dos catetos

longlado1 = float(input("Ingresa la longitud del primer cateto: "))
longlado2 = float(input("Ingresa la longitud del segundo cateto: "))
# Calcular la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(longlado1 * longlado1 + longlado2 * longlado2)
# Formatear la salida 
salida = ('Resumen del cálculo\n'
f'Cateto 1: {longlado1:.2f}\n'
f'Cateto 2: {longlado2:.2f}\n'
f'La hipotenusa del triángulo rectángulo es {hipotenusa:.4f}\n')

# Mostrar la salida con formato
print(salida)
