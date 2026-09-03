# p057-interes-simple.py
# Calcula los anios necesarios para alcanzar una meta de ahorro con interes simple.


while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Calculadora de Anios para Meta de Ahorro (Interes Simple)")
    print("-" * 60)

    while True:
        capital_inicial = float(input("Introduce el capital inicial: "))
        tasa_interes = float(input("Introduce la tasa de interes anual (%): "))
        meta_ahorro = float(input("Introduce la meta de ahorro: "))
        if capital_inicial > 0 and tasa_interes > 0 and meta_ahorro > capital_inicial:
            break
        else:
            print("Error: Asegurate de que los valores sean positivos y la meta sea mayor al capital inicial.")

    capital_actual = capital_inicial
    anios = 0
    interes_anual_fijo = capital_inicial * (tasa_interes / 100)

    while capital_actual <= meta_ahorro:
        capital_actual += interes_anual_fijo
        anios += 1

    print("\n" + "-" * 60)
    print(f"Para alcanzar o superar tu meta de ${meta_ahorro:,.2f}, necesitaras {anios} anios.")
    print(f"El monto final acumulado sera de ${capital_actual:,.2f}.")
    print("-" * 60)

    if input('\n¿Deseas realizar otro calculo (S/N)? ').upper() == 'N':
        break

print("\n\nGracias por utilizar este programa...")
