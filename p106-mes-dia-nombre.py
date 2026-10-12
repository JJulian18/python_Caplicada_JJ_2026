# ==================================================================
#  p106-mes-dia-nombre.py
#  Tarea 5 - Listas | Ejercicio 3: Nombre y dias del mes
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Leer un numero de mes (ej. 4). Guardar los dias de cada mes en una
#  lista y los nombres de los meses en otra lista (febrero = 28 dias).
#  Imprimir el nombre del mes y la cantidad de dias correspondiente.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : numero de mes (1-12).
#  Proceso : listas paralelas predefinidas nombres/dias; acceso por
#            indice (mes - 1).
#  Salida  : nombre del mes y sus dias.
#  Ejemplo : 4 -> Abril, 30
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Nombre y dias del mes")
print("-" * 60)

nombres = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
           "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
           "Diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Captura validada del numero de mes
while True:
    try:
        mes = int(input("Introduzca un número de mes (1-12): "))
        if 1 <= mes <= 12:
            break
        print("  El mes debe estar entre 1 y 12.")
    except ValueError:
        print("  Entrada invalida, debe ser un numero entero.")

indice = mes - 1                     # Las listas inician en el indice 0

print("\n--- Resultados ---")
print(f"Mes: {nombres[indice]}")
print(f"Días: {dias[indice]}")
