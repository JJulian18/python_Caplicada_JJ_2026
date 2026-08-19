# p011-operadores-asignacion.py
# Demostrar el uso de los operadores de asignación

print("\033[2J\033[H", end="", flush=True)

print("=" * 40)
print(" OPERADORES DE ASIGNACIÓN EN PYTHON")
print("=" * 40)
# Operador de asignación básico (=)
x = int(input("Ingresa un valor inicial para x: "))
print(f"Valor inicial de x: {x}")

# Aplicar diferentes operadores de asignación
x += 5
print(f"x += 5 → x = {x}") # Equivale a: x = x + 5
x -= 3
print(f"x -= 3 → x = {x}") # Equivale a: x = x - 3
x *= 2
print(f"x *= 2 → x = {x}") # Equivale a: x = x * 2
x /= 4
print(f"x /= 4 → x = {x}") # Equivale a: x = x / 4
x %= 3
print(f"x %= 3 → x = {x}") # Equivale a: x = x % 3
x **= 2
print(f"x **= 2 → x = {x}") # Equivale a: x = x ** 2
x //= 2
print(f"x //= 2 → x = {x}") # Equivale