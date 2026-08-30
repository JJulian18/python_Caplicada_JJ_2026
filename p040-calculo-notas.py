# p040-calculo-notas.py
# Calcular el promedio de 5 calificaciones y mostrar un mensaje segun el resultado.
print("\033[2J\033[H", end="", flush=True)
print('--- Calculo de Notas ---')
# Pedir al usuario las 5 calificaciones
notas = list(map(float, input('Ingresa 5 calificaciones: ').split()))
promedio = sum(notas) / len(notas)
print(f' Promedio: {promedio}')
# La estructura if/elif evalua el rango del promedio
if promedio < 6:
    print(' Quedas reprobado')
elif promedio < 7:
    print(' Pasas de panzazo')
elif promedio < 8:
    print(' Muy bien, puedes mejorar')
elif promedio < 9:
    print(' Excelente, sigue asi')
else:
    print(' Perfecto, tu esfuerzo valio la pena')
