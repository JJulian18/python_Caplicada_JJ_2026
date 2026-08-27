# p034-tipo-angulo.py
# Mostrar el tipo de ángulo según su medida en grados.
print("\033[2J\033[H", end="", flush=True)
print('--- Clasificador de Ángulos ---')
# Pedir al usuario que ingrese un ángulo
angulo = int(input('Dame un ángulo en grados: '))
# La estructura if/elif evalúa cada posible tipo de ángulo
if angulo < 0 or angulo >= 360:
# Este if de validación es útil para un mejor manejo de datos
    print(' El ángulo está fuera del rango de 0 a 360 grados.')
elif angulo < 90:
    print(f' El ángulo de {angulo} grados es un ángulo AGUDO.')
elif angulo == 90:
    print(f' El ángulo de {angulo} grados es un ángulo RECTO.')
elif angulo < 180:
    print(f' El ángulo de {angulo} grados es un ángulo OBTUSO.')
elif angulo == 180:
    print(f' El ángulo de {angulo} grados es un ángulo LLANO.')
elif angulo < 360:
    print(f' El ángulo de {angulo} grados es un ángulo CÓNCAVO.')
else: # En caso de que el ángulo sea exactamente 360
    print(f' El ángulo de {angulo} grados es un ángulo COMPLETO.')