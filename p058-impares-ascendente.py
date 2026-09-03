# p058-impares-ascendente.py
# Imprime los numeros impares y su suma en un rango ascendente de 1 a n.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Numeros Impares Ascendentes")
    print("-" * 60)

    n = int(input("Introduce un numero limite: "))

    numero = 1
    suma = 0
    impares = ""
    while numero <= n:
        if numero % 2 != 0:
            suma += numero
            if impares == "":
                impares = str(numero)
            else:
                impares += ", " + str(numero)
        numero += 1

    print(f"Numeros impares: {impares}")
    print(f"La suma de los impares es: {suma}")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
