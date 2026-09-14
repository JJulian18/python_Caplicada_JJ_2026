# p075-triangulo-caracter.py
# Imprime un triangulo rectangulo formado por un caracter, usando ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Triangulo de Caracter")
    print("-" * 60)

    n = int(input("Cuantos renglones tendra el triangulo? "))
    car = input("Que caracter quieres usar para dibujar? ")

    print("\n--- Triangulo Generado ---")

    # Ciclo exterior: controla los renglones
    for i in range(1, n + 1):
        # Ciclo interior: controla cuantos caracteres se imprimen en el renglon actual
        for j in range(i):
            print(car, end="")
        print()

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
