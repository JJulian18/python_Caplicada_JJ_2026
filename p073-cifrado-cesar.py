# p073-cifrado-cesar.py
# Cifra un mensaje usando el Cifrado Cesar, desplazando cada letra un numero de posiciones.

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Encriptador con Cifrado Cesar")
    print("-" * 60)

    mensaje_original = input("Ingresa el mensaje a encriptar: ")
    desplazamiento = int(input("Ingresa la clave de desplazamiento (un numero): "))

    mensaje_cifrado = ""
    for caracter in mensaje_original:
        if caracter.isalpha():  # Solo ciframos las letras
            codigo_ascii = ord(caracter)
            # Verificamos si es mayuscula o minuscula para mantener el caso
            base = ord('a') if caracter.islower() else ord('A')
            # Aplicamos la formula del cifrado
            codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
            mensaje_cifrado += chr(codigo_nuevo)
        else:
            mensaje_cifrado += caracter  # Los demas caracteres pasan igual

    print(f"\nMensaje Original: {mensaje_original}")
    print(f"Mensaje Cifrado: {mensaje_cifrado}")

    if input("\n\n¿Desea encriptar otro mensaje (S/N)? ").upper() == "N":
        break

print("\n\nEncriptacion finalizada...")
