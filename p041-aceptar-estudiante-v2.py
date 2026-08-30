# p041-aceptar-estudiante-v2.py
# Evaluar si un aspirante es aceptado en la "Universidad Kitty Kat SA".
print("\033[2J\033[H", end="", flush=True)
print('--- Admision Universidad Kitty Kat SA ---')
# Pedir los datos del aspirante
nombre = input('Nombre: ')
sexo = input('Sexo (h/m): ')
edad = int(input('Edad: '))
calificaciones = list(map(float, input('Calificaciones: ').split()))
promedio = sum(calificaciones) / len(calificaciones)
# La estructura if/elif evalua cada requisito en orden
if sexo != 'm':
    print(' Estudiante rechazado: no cumple con el requisito de sexo.')
elif edad <= 21:
    print(' Estudiante rechazado: no cumple con el requisito de edad.')
elif promedio < 8 or promedio > 9.5:
    print(' Estudiante rechazado: no cumple con el requisito de promedio.')
else:
    print(' Estudiante aceptado.')
