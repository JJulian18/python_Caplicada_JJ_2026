# p070-suma-pares-impares.py
# Imprime los numeros pares e impares de 1 a n, junto con sus sumas, usando un ciclo for.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Suma de Pares e Impares")
    print("-" * 60)

    n = int(input("Dame el valor final? "))

    suma_pares = 0
    suma_impares = 0
    cad_pares = ""
    cad_impares = ""

    for i in range(1, n + 1):
        if i % 2 == 0:
            suma_pares += i
            cad_pares += f" {i}"
        else:
            suma_impares += i
            cad_impares += f" {i}"

    print(f"\nLos pares: {cad_pares} = {suma_pares}")
    print(f"Los impares: {cad_impares} = {suma_impares}")

    if input("\n\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
