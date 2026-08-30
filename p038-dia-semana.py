# p038-dia-semana.py
# Mostrar el dia de la semana segun un numero del 1 al 7.
print("\033[2J\033[H", end="", flush=True)
print('--- Dias de la Semana ---')
# Pedir al usuario un numero del 1 al 7
numero = int(input('Dame un numero del 1 al 7: '))
# La estructura if/elif evalua cada dia posible
if numero == 1:
    print(' El dia es domingo.')
elif numero == 2:
    print(' El dia es lunes.')
elif numero == 3:
    print(' El dia es martes.')
elif numero == 4:
    print(' El dia es miercoles.')
elif numero == 5:
    print(' El dia es jueves.')
elif numero == 6:
    print(' El dia es viernes.')
elif numero == 7:
    print(' El dia es sabado.')
else: # En caso de que el numero este fuera del rango 1 a 7
    print(' El numero esta fuera del rango de 1 a 7.')
