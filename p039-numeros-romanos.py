# p039-numeros-romanos.py
# Mostrar el equivalente en numeros romanos de un numero del 1 al 10.
print("\033[2J\033[H", end="", flush=True)
print('--- Conversor a Numeros Romanos ---')
# Pedir al usuario un numero del 1 al 10
numero = int(input('Dame un numero del 1 al 10: '))
# La estructura if/elif evalua cada numero posible
if numero == 1:
    romano = 'I'
elif numero == 2:
    romano = 'II'
elif numero == 3:
    romano = 'III'
elif numero == 4:
    romano = 'IV'
elif numero == 5:
    romano = 'V'
elif numero == 6:
    romano = 'VI'
elif numero == 7:
    romano = 'VII'
elif numero == 8:
    romano = 'VIII'
elif numero == 9:
    romano = 'IX'
elif numero == 10:
    romano = 'X'
else: # En caso de que el numero este fuera del rango 1 a 10
    romano = None

if romano is None:
    print(' El numero esta fuera del rango de 1 a 10.')
else:
    print(f' El numero {numero} en romano es {romano}.')
