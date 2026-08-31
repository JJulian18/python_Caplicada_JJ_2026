# p051-adivina-numero.py
# Permite que el usuario realice multiples intentos hasta adivinar el numero secreto.
print("\033[2J\033[H", end="", flush=True)
import random

print('--- Adivina el Numero ---')

print('He pensado en un numero entre 1 y 50. puedes adivinarlo?')
print('------------------------------------------------------')
numero_secreto = random.randint(1, 50)  # Numero entero al azar entre 1 y 50.
contador_intentos = 0
# Usamos 'while True' para que el juego continúe hasta que adivinemos el número y rompamos el ciclo con 'break'.
while True:
    intento = int(input('Tu numero: '))
    contador_intentos += 1
    # Logica de pistas
    if intento < numero_secreto:
        print(' Demasiado bajo! Intenta con un numero mas alto.')
    elif intento > numero_secreto:
        print(' Demasiado alto! Intenta con un numero mas bajo.')
    else:
        # Si no es ni más bajo ni más alto, ¡es el correcto!
        print(f'\nFelicidades! Adivinaste el numero secreto que era {numero_secreto}!')
        print(f'Lo lograste en {contador_intentos} intentos.')
        break

print('\n Gracias por jugar!')
