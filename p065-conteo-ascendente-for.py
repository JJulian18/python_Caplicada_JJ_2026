# p065-conteo-ascendente-for.py
# Imprime los numeros de 1 a 100 usando un ciclo for.
print("\033[2J\033[H", end="", flush=True)

print('Iniciando secuencia de conteo ascendente...')
for i in range(1, 101, 1):
    print(f' {i}', end='')
print('\nSecuencia completada!')
