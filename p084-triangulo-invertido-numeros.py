# p084-triangulo-invertido-numeros.py
# Imprime un triangulo numerico invertido, de n renglones hasta llegar a un solo numero, con ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Triangulo Invertido de Numeros")
    print("-" * 60)

    n = int(input("Dame un numero: "))

    print()
    # Ciclo exterior: recorre cada renglon, de n hasta 1
    for i in range(n, 0, -1):
        fila = ""
        # Ciclo interior: imprime los numeros de 1 hasta i
        for j in range(1, i + 1):
            fila += str(j)
            if j < i:
                fila += " "
        print(fila)

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
