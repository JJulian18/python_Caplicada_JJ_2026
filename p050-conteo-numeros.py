# p050-conteo-numeros.py
# Lee numeros hasta ingresar 999, luego muestra un resumen estadistico.
print("\033[2J\033[H", end="", flush=True)


cuenta = 0
suma = 0
cuenta_positivos = 0
cuenta_negativos = 0
cuenta_ceros = 0

print('Analizador de Numeros (escribe 999 para finalizar)')

while True:
    num = int(input('Introduce un numero entero: '))
    if num == 999:  # Condicion de salida
        print('Detectado codigo de salida (999)')
        break  # Rompe el ciclo infinito.
    # Proceso
    cuenta += 1
    suma += num
    if num > 0:
        cuenta_positivos += 1
    elif num < 0:
        cuenta_negativos += 1
    else:
        cuenta_ceros += 1

print('\n--- Reporte ---')
print(f'Total de numeros introducidos: {cuenta}')
print(f'Suma de todos los numeros: {suma}')
print(f'Numeros positivos: {cuenta_positivos}')
print(f'Numeros negativos: {cuenta_negativos}')
print(f'Numeros en cero: {cuenta_ceros}')
