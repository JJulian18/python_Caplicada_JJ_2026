# p008-entrada-con-espacio.py
# Leer tres números enteros con espacio

print("\033[2J\033[H", end="", flush=True)

print('Dame tres números separados por espacio :')
n1, n2, n3 = input().split()
n1, n2, n3 = [ int(n1), int(n2), int(n3) ]
print('Los valores introducidos son:')
print(n1, n2, n3)