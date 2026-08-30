# p043-calculadora-anio-bisiesto.py
# Determinar si un anio es bisiesto.
print("\033[2J\033[H", end="", flush=True)
print('--- Calculadora de Anio Bisiesto ---')
# Pedir al usuario el anio
anio = int(input('Anio: '))
# Es bisiesto si es divisible entre 4 y no entre 100, o si es divisible entre 400
if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f' El anio {anio} es bisiesto.')
else:
    print(f' El anio {anio} no es bisiesto.')
