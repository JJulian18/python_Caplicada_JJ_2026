# p069-arriba-abajo.py
# Imprime numeros de 1 a n (arriba) o de n a 1 (abajo), segun elija el usuario, usando un ciclo for.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Imprimir Numeros Usando Ciclo For - Arriba o Abajo")
    print("-" * 60)
    print("[ 1 ] Imprimir numeros de 1 a n")
    print("[ 2 ] Imprimir numeros de n a 1")

    opcion = int(input("Que eliges? "))

    if opcion == 1:
        n = int(input("\nHasta donde? "))
        print(f"\nImprimir numeros de 1 a {n}")
        for x in range(1, n + 1, 1):
            print(x, end=' ')
    elif opcion == 2:
        n = int(input("\nDesde donde? "))
        print(f"\nImprimir numeros de {n} a 1")
        for x in range(n, 0, -1):
            print(x, end=' ')
    else:
        print("\nOpcion no valida")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
