# p004-paga-trabajador.py
# Calcular la paga total de un trabajador

print("\033[2J\033[H", end="", flush=True)
# Entradas

print('Calculando la paga de un trabajador')
print('Nombre : ')
nombre = input()
print('Horas trabajadas : ')
horas = int(input())
print('Paga por hora : ')
paga = float(input())

#Procesos

tasa = 0.03
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

#Salidas

print('Resumen de pagos:\n')
print(f'El trabajador {nombre}, trabajo {horas} horas, con una paga de {paga} pesos por hora, impuesto de {tasa}%')
print(f'Paga bruta: {pagabruta:>10.2f}')
print(f'Impuesto:   {impuesto:>10.2f}')
print(f'Paga neta:  {paganeta:>10.2f}')