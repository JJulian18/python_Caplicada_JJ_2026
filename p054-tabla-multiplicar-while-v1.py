# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla de multiplicar deseada t, hasta el multiplo n


while True:
    print("\033[2J\033[H", end="", flush=True)
    print('Imprime la tabla de multiplicar deseada t, hasta el multiplo n')

    while True:
        t = int(input('Que tabla quieres? '))
        n = int(input('Hasta donde la quieres? '))
        if t > 0 and n > 0:
            break
        print('Error, los numeros deben ser mayores que 0')

    c = 1
    while c <= n:
        print(f'{t} x {c} = {t*c}')
        c += 1

    if input('Deseas Continuar (S/N)? ').upper() == 'N':
        break

print("\n\nGracias por utilizar este programa...")
