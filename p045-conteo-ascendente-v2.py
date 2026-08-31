# p045-conteo-ascendente-v2.py
# Imprime los numeros de 1 a n, en incrementos de m, usando un ciclo while.
print("\033[2J\033[H", end="", flush=True)

print('Iniciando secuencia de conteo ascendente...')
n = int(input('Hasta donde? '))
m = int(input('De cuanto en cuanto? '))
c = 1
while c <= n:
    print(f' {c}', end='')
    c += m
print('\nSecuencia completada!')
