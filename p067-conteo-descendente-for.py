# p067-conteo-descendente-for.py
# Imprime los numeros de 100 a 1 usando un ciclo for.
print("\033[2J\033[H", end="", flush=True)

print('Iniciando cuenta regresiva...')
for x in range(100, 0, -1):
    print(f' {x}', end='')
print('\nDespegue!')
