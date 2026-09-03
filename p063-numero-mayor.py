# p063-numero-mayor.py
# Lee una serie de numeros hasta que se introduce un 0 y muestra el mayor.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Numero Mayor de una Serie")
    print("-" * 60)

    print("Introduce numeros (0 para terminar):")
    numero = int(input("> "))
    mayor = numero
    while numero != 0:
        if numero > mayor:
            mayor = numero
        numero = int(input("> "))

    print("-" * 20)
    print(f"El numero mayor fue: {mayor}")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
