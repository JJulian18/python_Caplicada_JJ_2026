# ==================================================================
#  p094-precio-acciones.py
#  Listas en Python - Parte 2 | Ejemplo 3: Precios de acciones
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Dada una lista de precios de cierre de una accion durante la
#  semana, encontrar el precio mas alto, el mas bajo y el dia en
#  que ocurrieron.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : listas fijas de dias y precios de cierre.
#  Proceso : max() y min() para los extremos; index() para obtener
#            la posicion y con ella el dia correspondiente.
#  Salida  : precios de la semana, maximo y minimo con su dia.
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Analisis basico de precios de una accion")
print("-" * 60)

# Precios de cierre de una accion (Lunes a Viernes)
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
precios = [150.25, 152.50, 149.75, 155.00, 153.20]

# Encontrar el precio maximo y minimo
precio_max = max(precios)
precio_min = min(precios)

# Encontrar la posicion (el dia) de esos precios
pos_max = precios.index(precio_max)
pos_min = precios.index(precio_min)

print(f"Precios de la semana: {precios}\n")
for i in range(len(dias)):
    print(f"{dias[i]:<10} ${precios[i]:>8.2f}")

print(f"\nEl precio mas alto fue ${precio_max:.2f} el dia {dias[pos_max]}.")
print(f"El precio mas bajo fue ${precio_min:.2f} el dia {dias[pos_min]}.")

print("\n\nGracias por utilizar este programa...")
