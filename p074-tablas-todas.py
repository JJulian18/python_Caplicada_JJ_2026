# p074-tablas-todas.py
# Imprime las tablas de multiplicar de 1 a n, cada una hasta el multiplicador m, usando ciclos for anidados.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Tablas de Multiplicar")
    print("-" * 60)

    n = int(input("Hasta que tabla de multiplicar deseas generar? "))
    m = int(input("Hasta que numero deseas multiplicar cada tabla? "))

    print("\n--- Generando Tablas de Multiplicar ---")

    # Ciclo exterior: recorre cada tabla (1, 2, 3... n)
    for i in range(1, n + 1):
        print(f"\n--- Tabla del {i} ---")
        # Ciclo interior: recorre cada multiplicador (1, 2... m)
        for j in range(1, m + 1):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
