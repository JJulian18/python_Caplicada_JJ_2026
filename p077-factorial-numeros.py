# p077-factorial-numeros.py
# Calcula e imprime el factorial de cada numero desde 1 hasta n, usando ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Calculo Sucesivo de Factoriales")
    print("-" * 60)

    try:
        n = int(input("Hasta que numero deseas calcular el factorial? "))

        # Ciclo exterior: recorre cada numero (1, 2, 3... n)
        for i in range(1, n + 1):
            factorial = 1  # Reiniciamos el factorial para cada nuevo numero

            # Ciclo interior: calcula el factorial de i (1 x 2 x 3 x ... x i)
            for j in range(1, i + 1):
                factorial *= j

            print(f"El factorial de {i}! es = {factorial}")
    except ValueError:
        print("Error: Por favor, introduce un numero entero valido.")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
