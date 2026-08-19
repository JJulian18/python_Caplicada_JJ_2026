
# p010-operaciones-matematicas
# Demostrar el uso de los diferentes operadores aritméticos con números

print("\033[2J\033[H", end="", flush=True)

print("=" * 50)
print(" CALCULADORA DE OPERACIONES MATEMÁTICAS")
print("=" * 50)
# Solicitar números al usuario
x = float(input('Ingresa el primer número (x): '))
y = float(input('Ingresa el segundo número (y): '))
print(f"\nRESULTADOS CON x = {x} y y = {y}")
print("-" * 40)
# Mostrar resultados directamente con formato alineado
print(f"Suma: {x:>6} + {y:<6} = {x + y:>10.2f}")
print(f"Resta: {x:>6} - {y:<6} = {x - y:>10.2f}")
print(f"Multiplicación: {x:>6} × {y:<6} = {x * y:>10.2f}")
print(f"División: {x:>6} ÷ {y:<6} = {x / y:>10.2f}")
print(f"Módulo: {x:>6} % {y:<6} = {x % y:>10.2f}")
print(f"Exponenciación: {x:>6} ^ {y:<6} = {x ** y:>10.2f}")
print(f"División entera: {x:>6} // {y:<6} = {x // y:>10.2f}")
print("=" * 50)