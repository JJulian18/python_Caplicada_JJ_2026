# p082-cuadro-hueco-caracter.py
# Dibuja un cuadrado hueco (solo el contorno) usando el caracter elegido, con ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Cuadrado Hueco de Caracter")
    print("-" * 60)

    n = int(input("¿De que tamano sera el lado del cuadrado? "))
    car = input("¿Que caracter quieres usar? ")

    print()
    # Ciclo exterior: recorre cada renglon del cuadrado
    for i in range(n):
        fila = ""
        # Ciclo interior: recorre cada columna del renglon actual
        for j in range(n):
            # El contorno son el primer y ultimo renglon, y la primera y ultima columna
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                fila += car
            else:
                fila += " "
            if j < n - 1:
                fila += " "
        print(fila)

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
