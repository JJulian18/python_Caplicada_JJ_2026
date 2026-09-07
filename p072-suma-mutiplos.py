# p072-suma-mutiplos.py
# Imprime los multiplos de m entre 1 y n, cuenta cuantos son y suma su valor, usando un ciclo for.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Multiplos de m Entre 1 y n")
    print("-" * 60)

    n = int(input("Hasta donde? "))
    m = int(input("Que multiplos quieres? "))

    cuenta_multiplos = 0
    suma_multiplos = 0
    for i in range(1, n + 1):
        if i % m == 0:
            print(i, end=' ')
            suma_multiplos += i
            cuenta_multiplos += 1

    print(f"\n\nFueron {cuenta_multiplos} multiplos, los cuales suman {suma_multiplos}")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
