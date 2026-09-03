# p059-pares-descendente.py
# Imprime los numeros pares y su suma en un rango descendente de 100 a n.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Numeros Pares Descendentes")
    print("-" * 60)

    n = int(input("Introduce un numero limite (menor a 100): "))

    numero = 100
    suma = 0
    pares = ""
    while numero >= n:
        if numero % 2 == 0:
            suma += numero
            if pares == "":
                pares = str(numero)
            else:
                pares += ", " + str(numero)
        numero -= 1

    print(f"Numeros pares: {pares}")
    print(f"La suma de los pares es: {suma}")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
