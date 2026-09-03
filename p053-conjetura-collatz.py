# p053-conjetura-collatz.py
# Calcula la conjetura de Collatz


while True:
    print("\033[2J\033[H", end="", flush=True)
    print('Imprime la conjetura de collatz')

    while True:
        num = int(input('Dame un numero = '))
        if num > 0:
            break
        print('Error, el numero debe ser mayor que 0')

    print('\nLa conjetura de collatz es:')
    while True:
        if num == 1:
            break
        print(num, end=' ')
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num, end=' ')

    if input('\n\nDeseas Continuar(S/N)? ').upper() == 'N':
        break

print("\n\nGracias por utilizar este programa...")
