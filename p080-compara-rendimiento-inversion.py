# p080-compara-rendimiento-inversion.py
# Compara el crecimiento de dos fondos de inversion a lo largo de varios anios, usando interes compuesto y un ciclo for.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Comparador de Fondos de Inversion")
    print("-" * 60)

    print("--- Fondo de Inversion A ---")
    monto_a = float(input("Monto inicial: "))
    tasa_a = float(input("Tasa de interes anual (%): "))

    print("\n--- Fondo de Inversion B ---")
    monto_b = float(input("Monto inicial: "))
    tasa_b = float(input("Tasa de interes anual (%): "))

    anios = int(input("\nAnios a proyectar: "))

    print("\n--- Comparacion de Rendimientos Anuales ---")
    print(f"{'Anio':<4} | {'Fondo A':<12} | {'Fondo B':<12}")
    print("-" * 43)

    # Ciclo for: recorre cada anio de la proyeccion
    for anio in range(1, anios + 1):
        saldo_a = monto_a * (1 + tasa_a / 100) ** anio
        saldo_b = monto_b * (1 + tasa_b / 100) ** anio
        print(f"{anio:>2} | $ {saldo_a:>9.2f} | $ {saldo_b:>9.2f}")

    if saldo_a > saldo_b:
        print(f"\nResultado final: El Fondo A (${saldo_a:.2f}) supero al Fondo B (${saldo_b:.2f}).")
    elif saldo_b > saldo_a:
        print(f"\nResultado final: El Fondo B (${saldo_b:.2f}) supero al Fondo A (${saldo_a:.2f}).")
    else:
        print(f"\nResultado final: Ambos fondos generaron el mismo rendimiento (${saldo_a:.2f}).")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
