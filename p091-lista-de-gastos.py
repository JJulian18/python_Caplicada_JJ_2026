# ==================================================================
#  p091-lista-de-gastos.py
#  Listas en Python - Parte 1 | Ejemplo 6: Control de Gastos
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Aplicacion que almacena gastos mensuales en una lista y permite
#  manipularla con un menu que se repite hasta que el usuario sale:
#   1. Ver Gastos      - muestra todos los gastos actuales.
#   2. Agregar Gasto   - pide un monto y lo anade a la lista.
#   3. Modificar Gasto - busca un gasto por indice y lo actualiza.
#   4. Eliminar Gasto  - busca un gasto por indice y lo elimina.
#   5. Ver Total       - calcula y muestra la suma de los gastos.
#   6. Salir           - termina el programa.
#  Requisitos tecnicos:
#   - try-except para que el programa no falle si se captura texto
#     en lugar de numeros.
#   - Feedback de exito o error en cada operacion
#     (ej. "Gasto no encontrado").
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : opcion del menu (str), montos (float), indices (int).
#  Proceso : while True para el menu; append() para agregar;
#            lista[i] = valor para modificar; pop(i) para eliminar;
#            for para recorrer y acumular el total.
#  Salida  : listado de gastos con su indice, total y mensajes de
#            confirmacion o error.
# ------------------------------------------------------------------
#  SUPUESTOS
#  - Los montos deben ser mayores que cero (se rechazan nan e inf).
#  - Los gastos se identifican por su indice (posicion en la lista),
#    que se muestra al listarlos.
# ==================================================================

gastos = []                  # list  - montos de los gastos registrados

while True:
    print("\033[2J\033[H", end="", flush=True)
    print("Control de Gastos Mensuales")
    print("-" * 60)
    print("1. Ver Gastos")
    print("2. Agregar Gasto")
    print("3. Modificar Gasto")
    print("4. Eliminar Gasto")
    print("5. Ver Total")
    print("6. Salir")
    print("-" * 60)

    opcion = input("Elige una opcion (1-6): ").strip()

    # ---------------------- 1. Ver gastos ----------------------
    if opcion == "1":
        print("\n--- Gastos registrados ---")
        if len(gastos) == 0:
            print("No hay gastos registrados.")
        else:
            print("Indice\tMonto")
            for i, gasto in enumerate(gastos):
                print(f"{i}\t${gasto:,.2f}")

    # ---------------------- 2. Agregar gasto -------------------
    elif opcion == "2":
        try:
            monto = float(input("\nMonto del gasto: $"))
            if not (0 < monto < float("inf")):
                print("Error: el monto debe ser un numero mayor que cero.")
            else:
                gastos.append(monto)
                print(f"Gasto de ${monto:,.2f} agregado con exito.")
        except ValueError:
            print("Error: debes introducir un numero valido.")

    # ---------------------- 3. Modificar gasto -----------------
    elif opcion == "3":
        if len(gastos) == 0:
            print("\nNo hay gastos para modificar.")
        else:
            print("\nIndice\tMonto")
            for i, gasto in enumerate(gastos):
                print(f"{i}\t${gasto:,.2f}")
            try:
                indice = int(input("\nIndice del gasto a modificar: "))
                if indice < 0 or indice >= len(gastos):
                    print("Error: Gasto no encontrado.")
                else:
                    nuevo = float(input("Nuevo monto: $"))
                    if not (0 < nuevo < float("inf")):
                        print("Error: el monto debe ser un numero mayor que cero.")
                    else:
                        anterior = gastos[indice]
                        gastos[indice] = nuevo
                        print(f"Gasto {indice} modificado: ${anterior:,.2f} -> ${nuevo:,.2f}")
            except ValueError:
                print("Error: debes introducir un numero valido.")

    # ---------------------- 4. Eliminar gasto ------------------
    elif opcion == "4":
        if len(gastos) == 0:
            print("\nNo hay gastos para eliminar.")
        else:
            print("\nIndice\tMonto")
            for i, gasto in enumerate(gastos):
                print(f"{i}\t${gasto:,.2f}")
            try:
                indice = int(input("\nIndice del gasto a eliminar: "))
                if indice < 0 or indice >= len(gastos):
                    print("Error: Gasto no encontrado.")
                else:
                    eliminado = gastos.pop(indice)
                    print(f"Gasto de ${eliminado:,.2f} eliminado con exito.")
            except ValueError:
                print("Error: debes introducir un numero entero valido.")

    # ---------------------- 5. Ver total -----------------------
    elif opcion == "5":
        total = 0.0
        for gasto in gastos:
            total += gasto
        print(f"\nNumero de gastos : {len(gastos)}")
        print(f"Total de gastos  : ${total:,.2f}")

    # ---------------------- 6. Salir ---------------------------
    elif opcion == "6":
        break

    else:
        print("\nError: opcion no valida, elige un numero del 1 al 6.")

    input("\nPresiona Enter para continuar...")

print("\n\nGracias por utilizar este programa...")
