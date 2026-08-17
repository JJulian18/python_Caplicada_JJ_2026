# p001-hola-mundo.py
# Lee datos y envia un saludo

print('Leyendo datos y enviando un saludo:\n')

# Leer datos
print("\033[2J\033[H", end="", flush=True)
nombre = input('Cual es tu nombre? ')
edad = int(input('Cual es tu edad? '))
peso = float(input('Cual es tu peso? '))

print(f'{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}')
# print(type(nombre))
# print(type(edad))
# print(type(peso))