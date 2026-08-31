# p049-sumar-consecutivos.py
# Suma numeros consecutivos hasta que el total sea >= 100, usando break.
print("\033[2J\033[H", end="", flush=True)

c = 0
suma = 0
print('Meta de ahorro: $100. Empezando a sumar numeros...')
# El ciclo esta programado para correr hasta 200, pero el break lo detendra antes.
while c < 200:
    c += 1
    suma += c
    print(f' (+{c})', end='')
    # Verificamos si hemos alcanzado o superado la meta.
    if suma >= 100:
        print('\n\nMeta alcanzada!')
        # La palabra break termina el ciclo inmediatamente.
        break
print(f'Se necesitaron los primeros {c} numeros para llegar a una suma de ${suma}.')
