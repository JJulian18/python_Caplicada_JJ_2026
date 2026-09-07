# p068-conteo-descendente-for-v2.py
# Imprime los numeros de n a 1, en decrementos de m, usando un ciclo for.
print("\033[2J\033[H", end="", flush=True)

print('Iniciando cuenta regresiva...')
n = int(input('Desde donde? '))
m = int(input('De cuanto en cuanto? '))
for x in range(n, 0, -m):
    print(f' {x}', end='')
print('\nDespegue!')
