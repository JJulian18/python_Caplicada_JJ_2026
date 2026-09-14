# p083-rombo-caracter.py
# Dibuja un rombo (diamante) de altura n usando el caracter elegido, con ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Rombo de Caracter")
    print("-" * 60)

    n = int(input("Dame un numero impar para la altura: "))
    car = input("¿Que caracter quieres usar? ")

    mitad = n // 2

    print()
    # Ciclo exterior: recorre cada renglon del rombo
    for i in range(n):
        # El nivel crece hasta la mitad y despues decrece (efecto espejo)
        nivel = i if i <= mitad else n - 1 - i
        espacios = mitad - nivel
        caracteres = 2 * nivel + 1

        # Primer ciclo interior: imprime los espacios en blanco a la izquierda
        for j in range(espacios):
            print(" ", end="")
        # Segundo ciclo interior: imprime los caracteres del renglon
        for k in range(caracteres):
            print(car, end="")

        print()

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
