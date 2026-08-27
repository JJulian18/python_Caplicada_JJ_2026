# p31-2da-ley-de-newton.py
# Calcular fuerza, masa o aceleración según la elección del usuario.
print("\033[2J\033[H", end="", flush=True)
print('--- Calculadora de la 2da Ley de Newton ---')
print('[1] Calcular la Fuerza (fuerza = masa * aceleración)')
print('[2] Calcular la Masa (masa = fuerza / aceleración)')
print('[3] Calcular la Aceleración (aceleración = fuerza / masa)')
opcion = int(input('Elige una opción (1, 2 o 3): '))
# La estructura if/elif/else ejecuta el cálculo correcto
if opcion == 1:
    print('\n Calculando la Fuerza...')
    masa = float(input('Dame la masa: '))
    aceleracion = float(input('Dame la aceleración: '))
    fuerza = masa * aceleracion
    print(f' La fuerza es: {fuerza} ')
elif opcion == 2:
    print('\n Calculando la Masa...')
    fuerza = float(input('Dame la fuerza: '))
    aceleracion = float(input('Dame la aceleración: '))
    masa = fuerza / aceleracion
    print(f' La masa es: {masa} ')
elif opcion == 3:
    print('\n Calculando la Aceleración...')
    fuerza = float(input('Dame la fuerza: '))
    masa = float(input('Dame la masa: '))
    aceleracion = fuerza / masa