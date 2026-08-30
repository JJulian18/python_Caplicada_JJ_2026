# p037-numero-mayor.py
# Identificar el mayor de tres numeros enteros.
print("\033[2J\033[H", end="", flush=True)
print('--- Comparador de Numeros ---')
# Pedir al usuario los tres numeros
a, b, c = map(int, input('Dame tres numeros: ').split())
# La estructura if/elif compara los numeros entre si
if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c
print(f' El mayor es {mayor}.')
