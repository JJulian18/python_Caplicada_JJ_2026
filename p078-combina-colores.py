# p078-combina-colores.py
# Genera todas las combinaciones posibles de dos colores a partir de una lista, usando ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Generador de Combinaciones de Colores")
    print("-" * 60)

    colores = input("Ingresa los colores separados por comas: ").strip().split(',')

    print(f"\nColores base: {colores}")
    print("--- Combinaciones Posibles ---")

    # Ciclo exterior: toma el primer color
    for color1 in colores:
        # Ciclo interior: toma el segundo color
        for color2 in colores:
            # Condicion para evitar combinar un color consigo mismo
            if color1 != color2:
                print(f"- {color1} y {color2}")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
