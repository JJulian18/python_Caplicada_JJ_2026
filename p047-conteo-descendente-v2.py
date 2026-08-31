# p047-conteo-descendente-v2.py
# Imprime los numeros de n a 1, en decrementos de m, usando un ciclo while.
print("\033[2J\033[H", end="", flush=True)

print('Iniciando cuenta regresiva...')
n = int(input('Desde donde? '))
m = int(input('De cuanto en cuanto? '))
c = n
while c >= 1:
    print(f' {c}', end='')
    c -= m
print('\nDespegue!')
