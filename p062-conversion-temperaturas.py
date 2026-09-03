# p062-conversion-temperaturas.py
# Convierte un rango de temperaturas de grados Celsius a Fahrenheit.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Conversion de Temperaturas: Celsius a Fahrenheit")
    print("-" * 60)

    inicial = int(input("Introduce la temperatura inicial en °C: "))
    final = int(input("Introduce la temperatura final en °C: "))

    print("-" * 20)
    celsius = inicial
    while celsius <= final:
        fahrenheit = celsius * 9 / 5 + 32
        print(f"{celsius}°C = {fahrenheit}°F")
        celsius += 1

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
