# p046-conteo-descendente.py
# Imprime los numeros de 100 a 1 usando un ciclo while.
print("\033[2J\033[H", end="", flush=True)

print('Iniciando cuenta regresiva...')
c = 100
while c >= 1:
    print(f' {c}', end='')
    c -= 1
print('\nDespegue!')
