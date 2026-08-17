# p003-area-triangulo.py
# Calcular el área de un triángulo

print("\033[2J\033[H", end="", flush=True)

print('Calculando el área de un triangulo:\n')
print('Dame la base y la altura separados por Enter')

base, altura = int(input()), int(input())
area = base * altura / 2

print(f'El triángulo de base {base} y altura {altura} tiene un area de {area}')