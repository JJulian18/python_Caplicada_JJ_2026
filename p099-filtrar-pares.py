# ==================================================================
#  p099-filtrar-pares.py
#  Listas en Python - Parte 3 | Ejemplo 2: Filtrar numeros pares
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Separar numeros pares:
#   - Solicitar una cantidad de numeros enteros y almacenarlos en
#     una lista.
#   - Crear una segunda lista que contenga unicamente los valores
#     pares usando una comprension con filtro (if).
#   - Mostrar ambas listas y la cantidad de pares encontrados.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : cantidad (int) y cada numero entero.
#  Proceso : for + append() para capturar;
#            [numero for numero in numeros if numero % 2 == 0].
#  Salida  : lista original, lista de pares y len(pares).
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Filtro de numeros pares")
print("-" * 60)


def leer_entero(mensaje):
    """Solicita un entero hasta que la entrada sea valida."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no valida. Por favor, introduce un numero entero.")


cantidad = leer_entero("Cuantos numeros capturaras? ")
while cantidad < 0:
    print("Error: la cantidad no puede ser negativa.")
    cantidad = leer_entero("Cuantos numeros capturaras? ")

numeros = []
for i in range(cantidad):
    numeros.append(leer_entero(f"Numero {i + 1}: "))

# Comprension con filtro: solo se agregan los pares
pares = [numero for numero in numeros if numero % 2 == 0]

print(f"\nLista original   : {numeros}")
print(f"Numeros pares    : {pares}")
print(f"Cantidad de pares: {len(pares)}")
