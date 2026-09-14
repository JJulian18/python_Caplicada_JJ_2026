# p079-suma-potencias.py
# Calcula la suma de las potencias de x desde x^1 hasta x^n, usando ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Suma de Potencias")
    print("-" * 60)

    x = float(input("Introduce el valor de x: "))
    n = int(input("Introduce el numero de terminos (n): "))
    suma_total = 0

    print(f"\nCalculando la serie S = x^1 + ... + x^{n}")

    # Ciclo exterior: recorre cada termino de la serie
    for i in range(1, n + 1):
        termino_actual = 1

        # Ciclo interior: calcula la potencia x^i
        for j in range(i):
            termino_actual *= x

        print(f"Termino {i}: {x}^{i} = {termino_actual}")
        suma_total += termino_actual

    print(f"\nEl resultado de la serie es: {suma_total}")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
