# p071-suma-promedio-numeros.py
# Suma y calcula el promedio de n numeros introducidos por el usuario, usando un ciclo for.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Suma y Promedio de Numeros")
    print("-" * 60)

    cuantos = int(input("Cuantos numeros deseas procesar? "))

    suma = 0
    cad_numeros = ""
    for i in range(1, cuantos + 1):
        numero = int(input(f"Numero[{i}] = "))
        suma += numero
        cad_numeros += f" {numero}"

    promedio = suma / cuantos
    print(f"\nLos numeros que introdujiste fueron:{cad_numeros}")
    print(f"La suma es {suma}, el promedio es {promedio}")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
