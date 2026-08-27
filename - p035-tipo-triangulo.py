# p035-tipo-triangulo.py
# Objetivo: Clasificar un triángulo según la longitud de sus tres lados.

print("\033[2J\033[H", end="", flush=True)
print("--- CLASIFICADOR DE TRIÁNGULOS ---")
print("Ingresa la longitud de los tres lados de un triángulo.")

# Solicitar la longitud de los lados
lado_a = float(input("Ingresa la longitud del primer lado: "))
lado_b = float(input("Ingresa la longitud del segundo lado: "))
lado_c = float(input("Ingresa la longitud del tercer lado: "))

# Usar la sentencia elif para verificar las condiciones en orden
if lado_a == lado_b and lado_b == lado_c:
    print(f" Es un triángulo EQUILÁTERO (todos los lados son iguales).")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print(f" Es un triángulo ISÓSCELES (al menos dos lados son iguales).")
else:
    print(f" Es un triángulo ESCALENO (ningún lado es igual).")