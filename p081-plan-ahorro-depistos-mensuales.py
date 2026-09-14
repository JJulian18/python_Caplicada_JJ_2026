# p081-plan-ahorro-depistos-mensuales.py
# Simula un plan de ahorro con depositos mensuales fijos e interes compuesto mensual, usando un ciclo for.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Simulador de Plan de Ahorro")
    print("-" * 60)

    monto_inicial = float(input("Monto inicial de ahorro: "))
    deposito = float(input("Deposito mensual: "))
    tasa = float(input("Tasa de interes mensual (%): "))
    meses = int(input("Numero de meses a simular: "))

    print("\n--- Plan de Ahorro Detallado ---")

    saldo = monto_inicial
    # Ciclo for: recorre cada mes del plan de ahorro
    for mes in range(1, meses + 1):
        saldo_inicial = saldo
        # El interes se calcula sobre el saldo inicial, antes de sumar el nuevo deposito
        interes = saldo_inicial * (tasa / 100)
        saldo = saldo_inicial + interes + deposito
        print(f"Mes {mes}: Saldo Inicial: ${saldo_inicial:.2f} | Interes: ${interes:.2f} | Saldo Final: ${saldo:.2f}")

    print(f"\nAl final de {meses} meses, tendras ${saldo:.2f}")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
