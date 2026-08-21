# p019-calculo-tiempo
# Convertir una cantidad de horas a días, minutos y segundos
print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario la cantidad de horas
horas = int(input("Ingresa la cantidad de horas: "))
# Calcular el equivalente en días, minutos y segundos
dias = horas / 24
minutos = horas * 60
segundos = horas * 60 * 60
# Formatear la salida 
salida = ('Resumen del cálculo\n'
f'Horas: {horas}\n'
f'Equivalen a {dias:.2f} días\n'
f'Equivalen a {minutos} minutos\n'
f'Equivalen a {segundos} segundos\n')
# Mostrar la salida con formato
print(salida)