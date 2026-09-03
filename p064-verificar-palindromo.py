# p064-verificar-palindromo.py
# Verifica si un numero entero es palindromo.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Verificar si un Numero es Palindromo")
    print("-" * 60)

    numero = int(input("Introduce un numero para verificar si es palindromo: "))

    original = numero
    reverso = 0
    while numero > 0:
        digito = numero % 10
        reverso = reverso * 10 + digito
        numero //= 10

    if original == reverso:
        print(f"El numero {original} es un palindromo.")
    else:
        print(f"El numero {original} no es un palindromo.")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
