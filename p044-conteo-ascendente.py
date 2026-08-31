# p044-conteo-ascendente.py
# Imprime los numeros de 1 a 100 usando un ciclo while.
print("\033[2J\033[H", end="", flush=True)

print('Iniciando secuencia de conteo ascendente...')

c = 1
while c <= 100:
    print(f' {c}', end='')
    c += 1
print('\nSecuencia completada!')
