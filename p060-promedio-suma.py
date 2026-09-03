# p060-promedio-suma.py
# Lee numeros hasta que se introduce un 0 y muestra el conteo, la suma y el promedio.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Promedio y Suma de una Serie de Numeros")
    print("-" * 60)

    print("Introduce numeros (0 para terminar):")
    suma = 0
    contador = 0
    numero = int(input("> "))
    while numero != 0:
        suma += numero
        contador += 1
        numero = int(input("> "))

    print("-" * 20)
    if contador > 0:
        promedio = suma / contador
        print(f"Se introdujeron {contador} numeros.")
        print(f"La suma es: {suma}")
        print(f"El promedio es: {promedio}")
    else:
        print("No se introdujo ningun numero.")

    if input("\n¿Desea continuar (S/N)? ").upper() == "N":
        break

print("\n\nGracias por utilizar este programa...")
