# p036-numeros-consecutivos.py
# Determinar si tres numeros enteros son consecutivos.
print("\033[2J\033[H", end="", flush=True)
print('--- Verificador de Numeros Consecutivos ---')
# Pedir al usuario los tres numeros
a, b, c = map(int, input('Dame tres numeros: ').split())
# Son consecutivos si cada uno es uno mas que el anterior
if b == a + 1 and c == b + 1:
    print(f' Los numeros {a}, {b}, {c} son consecutivos.')
else:
    print(f' Los numeros {a}, {b}, {c} no son consecutivos.')
