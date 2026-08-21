# p022-resistencia-equivalente-paralelo
# Calcular la resistencia equivalente de cuatro resistencias en paralelo
print("\033[2J\033[H", end="", flush=True)

# Solicitar al usuario el valor de cada una de las cuatro resistencias
r1 = float(input("Ingresa el valor de R1 (ohms): "))
r2 = float(input("Ingresa el valor de R2 (ohms): "))
r3 = float(input("Ingresa el valor de R3 (ohms): "))
r4 = float(input("Ingresa el valor de R4 (ohms): "))
# Calcular la resistencia total del circuito en paralelo
rtotal = 1 / (1 / r1 + 1 / r2 + 1 / r3 + 1 / r4)
# Formatear la salida
salida = ('Resumen del cálculo\n'
f'R1: {r1:.2f} ohms\n'
f'R2: {r2:.2f} ohms\n'
f'R3: {r3:.2f} ohms\n'
f'R4: {r4:.2f} ohms\n'
f'La resistencia total del circuito es {rtotal:.4f} ohms\n')
# Mostrar la salida con formato
print(salida)