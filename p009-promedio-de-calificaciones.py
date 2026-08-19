# p009-promedio-de-calificaciones
# Objetivo: Calcular el promedio de tres calificaciones ingresadas por el usuario.
print("\033[2J\033[H", end="", flush=True)

print('Calculando el promedio de tres calificaciones:\n')
# Solicitar las calificaciones en una sola línea separadas por espacio
print('Dame 3 calificaciones separadas por espacios:')
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 = int(cal1), int(cal2), int(cal3)
# Calcular el promedio
promedio = (cal1 + cal2 + cal3) / 3
# Mostrar el resultado incluyendo las calificaciones
print(f'Las calificaciones son: {cal1}, {cal2}, {cal3}')
print(f'El promedio de las calificaciones es: {promedio}')