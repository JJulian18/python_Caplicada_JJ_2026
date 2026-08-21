# p020-numero-suerte
# Mostrar los dígitos individuales de un año y calcular su suma
print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario su año de nacimiento
epoca = input("Ingresa tu año de nacimiento (cuatro dígitos): ")
# Extraer cada uno de los dígitos individuales del año
digito1 = epoca[0]
digito2 = epoca[1]
digito3 = epoca[2]
digito4 = epoca[3]
# Calcular la suma de los dígitos individuales
suma = int(digito1) + int(digito2) + int(digito3) + int(digito4)
# Formatear la salida 
salida = ('Resumen del cálculo\n'
f'Año de nacimiento: {epoca}\n'
f'Dígitos: "{digito1}", "{digito2}", "{digito3}", "{digito4}"\n'
f'La suma de los dígitos es: {suma}\n')
# Mostrar la salida con formato
print(salida)
