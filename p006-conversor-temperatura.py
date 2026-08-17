# p006-conversor-temperatura.py
# Convertir temperatura de Celsius a Fahrenheit

print("\033[2J\033[H", end="", flush=True)

print("Conversor de Temperatura (Celsius a Fahrenheit):\n")
celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")