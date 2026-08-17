# p002-area-circulo.py
# Calcular el area de un círculo
import math



print('Calculando el área de un circulo:\n')

print('Dame el radio: ')

radio = float(input())
area = math.pi * math.pow(radio,2)

print(f'El círculo de radio {radio:.2f} tiene un area de {area:.2f}')