# p048-multiplos-continue.py
# Imprime solo los multiplos de 10 hasta 200.
print("\033[2J\033[H", end="", flush=True)

print('Buscando multiplos de 10 entre 1 y 200...')
c = 0
while c < 200:
    c += 1
    if c % 10 != 0:
        # Ignora todo lo que sigue y salta a la siguiente iteracion.
        continue
   # Esta línea SÓLO se ejecuta si el 'if' fue falso (es decir, si es un múltiplo de 10).
    print(f' {c}', end=' ')
print('\nBusqueda finalizada.')
