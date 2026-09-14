# p076-piramide-caracter.py
# Imprime una piramide formada por un caracter, usando ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Piramide de Caracter")
    print("-" * 60)

    altura = int(input("Introduce la altura de la piramide: "))
    car = input("Introduce el caracter para la piramide: ")

    print("\n--- Piramide Generada ---")

    # Ciclo exterior: recorre cada nivel de la piramide
    for i in range(1, altura + 1):
        espacios = altura - i
        caracteres = 2 * i - 1

        # Primer ciclo interior: imprime los espacios en blanco a la izquierda
        for j in range(espacios):
            print(" ", end="")

        # Segundo ciclo interior: imprime los caracteres
        for k in range(caracteres):
            print(car, end="")

        print()

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
