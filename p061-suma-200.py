# p061-suma-200.py
# Suma numeros introducidos hasta alcanzar o superar una meta de 200.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Suma hasta Alcanzar la Meta de 200")
    print("-" * 60)

    meta = 200
    suma = 0
    contador = 0
    while suma < meta:
        numero = int(input(f"Suma actual: {suma}. Introduce un numero: "))
        suma += numero
        contador += 1

    print("-" * 20)
    print(f"Meta de {meta} alcanzada.")
    print(f"Suma final: {suma}")
    print(f"Total de numeros introducidos: {contador}")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
