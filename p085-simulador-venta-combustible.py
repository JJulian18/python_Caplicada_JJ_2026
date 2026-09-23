# ==================================================================
#  p085_SimuladorVentaCombustible.py
# ------------------------------------------------------------------
#  Examen Práctico Complementario: Programación Python
#  Materia:     Computación Aplicada
#  Ciclo:       Semestre Agosto-Diciembre 2026
#  Catedrático: Carlos Héctor Castañeda Ramírez
#  Alumno:      Josué Julián Ramírez Rosales
#  Matrícula:   20202162
#  Fecha:       22/09/2026
# ------------------------------------------------------------------
#  DESCRIPCIÓN
#  Sistema interactivo de consola para una estación de servicio.
#  Permite registrar ventas de combustible, simular el rendimiento
#  de un vehículo a 12 meses y clasificar clientes según su volumen
#  de compra mensual.
# ------------------------------------------------------------------
#  SUPUESTOS DE DISEÑO (vacíos del enunciado resueltos)
#  1. Tipo de combustible: submenú validado (1 Magna, 2 Premium,
#     3 Diésel) que muestra el precio de lista de cada uno.
#  2. Precios: cada combustible tiene un precio de lista (constante).
#     - Venta: el operador lo acepta con Enter o captura otro.
#       Si el precio de lista es 0.0, se obliga a capturarlo.
#     - Simulación: se usa el precio de lista; si es 0.0, se pide.
#  3. Capacidad de tanque: 40 L, usada para calcular tanques
#     completos (//) y litros sobrantes (%).
#  4. Simulación: 12 periodos mensuales RELATIVOS (Mes 1 = primer
#     mes proyectado), no meses del calendario.
#     Consumo mensual (L) = km mensuales / rendimiento (km/L).
#  5. Aumento de precio: 1 % mensual compuesto, aplicado con (**).
#  6. Clasificador:  Regular  < 100 L
#                    Premium  100 L a 500 L (ambos incluidos)
#                    Flotilla > 500 L
#  7. Validación: los datos inválidos se vuelven a pedir en un
#     ciclo while. Se valida con str.isdecimal() (sin try/except).
#  8. Km inicial y litros del clasificador aceptan 0 (>= 0);
#     precio, litros de venta, km mensuales y rendimiento, > 0.
#  9. Al salir se muestra un resumen de las VENTAS de la sesión.
# 10. Tope de captura: ningún dato numérico puede superar 1,000,000.
#     Evita que un número gigante se vuelva "inf" y rompa los cálculos.
# ------------------------------------------------------------------
#  RESTRICCIONES RESPETADAS (Bloque 1)
#  Sin listas, tuplas, diccionarios ni funciones personalizadas.
#  Solo tipos int, float y str; control con while/for/if.
# ==================================================================


# ─────────────────────────── CONSTANTES ───────────────────────────
CAPACIDAD_TANQUE = 40        # int   - litros por tanque estándar
PRECIO_MAGNA = 23.99           # float - precio de lista ($/L)
PRECIO_PREMIUM =28.99        # float - precio de lista ($/L)
PRECIO_DIESEL = 27.00        # float - precio de lista ($/L)
TASA_AUMENTO = 0.01          # float - aumento mensual del precio (1 %)
MESES = 12                   # int   - periodos de la simulación
LIMITE_PREMIUM = 100         # int   - litros mínimos para Premium
LIMITE_FLOTILLA = 500        # int   - litros máximos para Premium
VALOR_MAXIMO = 1000000       # int   - tope de cualquier captura numérica
ANCHO = 50                   # int   - ancho de la consola
LINEA = "═" * ANCHO          # str   - separador principal
SUBLINEA = "─" * ANCHO       # str   - separador secundario


# ───────────────────── ACUMULADORES DE SESIÓN ─────────────────────
num_ventas = 0               # int   - ventas registradas
litros_vendidos = 0.0        # float - litros vendidos en total
total_recaudado = 0.0        # float - dinero recaudado en total


# ─────────────────────── VARIABLES DE TRABAJO ─────────────────────
# Generales
opcion = ""                  # str   - opción del menú principal
op_tipo = ""                 # str   - opción del submenú de combustible
texto = ""                   # str   - entrada del usuario antes de validarla
tipo = ""                    # str   - tipo de combustible
precio_lista = 0.0           # float - precio de lista del combustible elegido
precio = 0.0                 # float - precio por litro aplicado

# Módulo 1: Venta
litros = 0.0                 # float - litros de la venta
total = 0.0                  # float - total de la venta
tanques = 0                  # int   - tanques completos de 40 L
sobrante = 0.0               # float - litros que no completan un tanque

# Módulo 2: Simulación
km_inicial = 0.0             # float - kilometraje inicial del vehículo
km_mensuales = 0.0           # float - km recorridos por mes
rendimiento = 0.0            # float - rendimiento del vehículo (km/L)
odometro = 0.0               # float - kilometraje al cierre de cada mes
litros_mes = 0.0             # float - litros consumidos por mes
precio_mes = 0.0             # float - precio por litro en ese mes
costo_mes = 0.0              # float - costo del combustible en ese mes
litros_total = 0.0           # float - litros de los 12 meses
costo_total = 0.0            # float - costo de los 12 meses

# Módulo 3: Clasificador
litros_cliente = 0.0         # float - compra mensual del cliente (L)
categoria = ""               # str   - Regular / Premium / Flotilla


# ─────────────────────── PROGRAMA PRINCIPAL ───────────────────────
while True:
    print()
    print(LINEA)
    print(f"{'ESTACIÓN DE SERVICIO':^{ANCHO}}")
    print(f"{'Sistema de Venta de Combustible':^{ANCHO}}")
    print(LINEA)
    print("  1. Venta de combustible")
    print("  2. Simulación de rendimiento")
    print("  3. Clasificador de cliente")
    print("  4. Salir")
    print(SUBLINEA)
    opcion = input("  Elige una opción (1-4): ").strip()

    # Opción inválida: se avisa y se regresa al menú (continue salta
    # la pausa del final del ciclo)
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        print("  [!] Opción inválida. Elige un número del 1 al 4.")
        continue

    # ════════════════ MÓDULO 1: VENTA DE COMBUSTIBLE ════════════════
    if opcion == "1":
        print()
        print(LINEA)
        print(f"{'VENTA DE COMBUSTIBLE':^{ANCHO}}")
        print(LINEA)

        # 1.1 Selección del tipo de combustible (asigna el precio de lista)
        while True:
            print(f"  1. Magna     ${PRECIO_MAGNA:>8,.2f} /L")
            print(f"  2. Premium   ${PRECIO_PREMIUM:>8,.2f} /L")
            print(f"  3. Diésel    ${PRECIO_DIESEL:>8,.2f} /L")
            op_tipo = input("  Selecciona el combustible (1-3): ").strip()
            if op_tipo == "1":
                tipo = "Magna"
                precio_lista = PRECIO_MAGNA
                break
            elif op_tipo == "2":
                tipo = "Premium"
                precio_lista = PRECIO_PREMIUM
                break
            elif op_tipo == "3":
                tipo = "Diésel"
                precio_lista = PRECIO_DIESEL
                break
            print("  [!] Opción inválida. Elige 1, 2 o 3.")

        # 1.2 Precio por litro (Enter = precio de lista; o se captura otro)
        while True:
            texto = input(f"  Precio por litro [Enter = ${precio_lista:,.2f}]: ").strip()
            if texto == "" and precio_lista > 0:
                precio = precio_lista
                break
            elif texto.replace(".", "", 1).isdecimal() and float(texto) > 0 and float(texto) <= VALOR_MAXIMO:
                precio = float(texto)
                break
            print(f"  [!] Ingresa un precio mayor a 0 y hasta {VALOR_MAXIMO:,}.")

        # 1.3 Captura y validación de los litros a vender
        while True:
            texto = input("  Litros a cargar: ").strip()
            if texto.replace(".", "", 1).isdecimal() and float(texto) > 0 and float(texto) <= VALOR_MAXIMO:
                litros = float(texto)
                break
            print(f"  [!] Ingresa litros mayor a 0 y hasta {VALOR_MAXIMO:,}.")

        # 1.4 Cálculos de la venta
        total = precio * litros
        tanques = int(litros // CAPACIDAD_TANQUE)
        sobrante = litros % CAPACIDAD_TANQUE

        # 1.5 Ticket de venta
        print()
        print(LINEA)
        print(f"{'TICKET DE VENTA':^{ANCHO}}")
        print(LINEA)
        print(f"  {'Combustible:':<20}{tipo:>28}")
        print(f"  {'Precio por litro:':<20}${precio:>27,.2f}")
        print(f"  {'Litros cargados:':<20}{litros:>26,.2f} L")
        print(SUBLINEA)
        print(f"  {'Tanques de ' + str(CAPACIDAD_TANQUE) + ' L:':<20}{tanques:>28}")
        print(f"  {'Litros sobrantes:':<20}{sobrante:>26,.2f} L")
        print(SUBLINEA)
        print(f"  {'TOTAL A PAGAR:':<20}${total:>27,.2f}")
        print(LINEA)

        # Actualización de acumuladores de sesión
        num_ventas += 1
        litros_vendidos += litros
        total_recaudado += total

    # ════════════════ MÓDULO 2: SIMULACIÓN DE RENDIMIENTO ═══════════
    elif opcion == "2":
        print()
        print(LINEA)
        print(f"{'SIMULACIÓN DE RENDIMIENTO':^{ANCHO}}")
        print(LINEA)

        # 2.1 Selección del combustible (mismo submenú del 1.1)
        while True:
            print(f"  1. Magna     ${PRECIO_MAGNA:>8,.2f} /L")
            print(f"  2. Premium   ${PRECIO_PREMIUM:>8,.2f} /L")
            print(f"  3. Diésel    ${PRECIO_DIESEL:>8,.2f} /L")
            op_tipo = input("  Selecciona el combustible (1-3): ").strip()
            if op_tipo == "1":
                tipo = "Magna"
                precio_lista = PRECIO_MAGNA
                break
            elif op_tipo == "2":
                tipo = "Premium"
                precio_lista = PRECIO_PREMIUM
                break
            elif op_tipo == "3":
                tipo = "Diésel"
                precio_lista = PRECIO_DIESEL
                break
            print("  [!] Opción inválida. Elige 1, 2 o 3.")

        # Se usa el precio de lista; si no está definido (0.0), se pide
        precio = precio_lista
        while precio <= 0:
            texto = input("  Sin precio de lista. Precio por litro ($): ").strip()
            if texto.replace(".", "", 1).isdecimal() and float(texto) > 0 and float(texto) <= VALOR_MAXIMO:
                precio = float(texto)
            else:
                print(f"  [!] Ingresa un precio mayor a 0 y hasta {VALOR_MAXIMO:,}.")

        # 2.2 Kilometraje inicial (acepta 0: vehículo nuevo)
        while True:
            texto = input("  Kilometraje inicial (km): ").strip()
            if texto.replace(".", "", 1).isdecimal() and float(texto) <= VALOR_MAXIMO:
                km_inicial = float(texto)
                break
            print(f"  [!] Ingresa un número de 0 a {VALOR_MAXIMO:,}.")

        # 2.3 Kilómetros recorridos por mes
        while True:
            texto = input("  Km recorridos por mes: ").strip()
            if texto.replace(".", "", 1).isdecimal() and float(texto) > 0 and float(texto) <= VALOR_MAXIMO:
                km_mensuales = float(texto)
                break
            print(f"  [!] Ingresa km mayor a 0 y hasta {VALOR_MAXIMO:,}.")

        # 2.4 Rendimiento del vehículo
        while True:
            texto = input("  Rendimiento del vehículo (km/L): ").strip()
            if texto.replace(".", "", 1).isdecimal() and float(texto) > 0 and float(texto) <= VALOR_MAXIMO:
                rendimiento = float(texto)
                break
            print(f"  [!] Ingresa un rendimiento mayor a 0 y hasta {VALOR_MAXIMO:,}.")

        # 2.5 Tabla de proyección a 12 meses
        litros_total = 0.0
        costo_total = 0.0
        print()
        print(LINEA)
        print(f"{'PROYECCIÓN A ' + str(MESES) + ' MESES - ' + tipo.upper():^{ANCHO}}")
        print(LINEA)
        print(f"  {'Mes':>3} {'Odómetro':>12} {'Litros':>9} {'$/L':>9} {'Costo $':>11}")
        print(SUBLINEA)
        for mes in range(1, MESES + 1):
            odometro = km_inicial + km_mensuales * mes
            litros_mes = km_mensuales / rendimiento
            precio_mes = precio * (1 + TASA_AUMENTO) ** (mes - 1)
            costo_mes = litros_mes * precio_mes
            litros_total += litros_mes
            costo_total += costo_mes
            print(f"  {mes:>3} {odometro:>12,.1f} {litros_mes:>9,.2f}"
                  f" {precio_mes:>9,.2f} {costo_mes:>11,.2f}")
        print(SUBLINEA)
        print(f"  {'Kilometraje final:':<20}{odometro:>25,.1f} km")
        print(f"  {'Litros totales:':<20}{litros_total:>26,.2f} L")
        print(f"  {'COSTO TOTAL:':<20}${costo_total:>27,.2f}")
        print(LINEA)

    # ════════════════ MÓDULO 3: CLASIFICADOR DE CLIENTE ═════════════
    elif opcion == "3":
        print()
        print(LINEA)
        print(f"{'CLASIFICADOR DE CLIENTE':^{ANCHO}}")
        print(LINEA)

        # 3.1 Compra mensual del cliente (acepta 0)
        while True:
            texto = input("  Litros comprados al mes: ").strip()
            if texto.replace(".", "", 1).isdecimal() and float(texto) <= VALOR_MAXIMO:
                litros_cliente = float(texto)
                break
            print(f"  [!] Ingresa un número de 0 a {VALOR_MAXIMO:,}.")

        # 3.2 Clasificación con if/elif/else y operador lógico and
        if litros_cliente < LIMITE_PREMIUM:
            categoria = "Regular"
        elif litros_cliente >= LIMITE_PREMIUM and litros_cliente <= LIMITE_FLOTILLA:
            categoria = "Premium"
        else:
            categoria = "Flotilla"

        # 3.3 Resultado
        print(SUBLINEA)
        print(f"  {'Compra mensual:':<20}{litros_cliente:>26,.2f} L")
        print(f"  {'CATEGORÍA:':<20}{categoria:>28}")
        print(SUBLINEA)
        print(f"  Regular <{LIMITE_PREMIUM} | Premium {LIMITE_PREMIUM}-{LIMITE_FLOTILLA}"
              f" | Flotilla >{LIMITE_FLOTILLA} L")
        print(LINEA)

    # ════════════════ MÓDULO 4: SALIR ═══════════════════════════════
    elif opcion == "4":
        print()
        print(LINEA)
        print(f"{'RESUMEN DE LA SESIÓN':^{ANCHO}}")
        print(LINEA)
        if num_ventas == 0:
            print(f"{'No se registraron ventas en esta sesión.':^{ANCHO}}")
        else:
            print(f"  {'Ventas realizadas:':<20}{num_ventas:>28}")
            print(f"  {'Litros vendidos:':<20}{litros_vendidos:>26,.2f} L")
            print(f"  {'Promedio por venta:':<20}${total_recaudado / num_ventas:>27,.2f}")
            print(SUBLINEA)
            print(f"  {'TOTAL RECAUDADO:':<20}${total_recaudado:>27,.2f}")
        print(LINEA)
        print(f"{'Gracias por usar el sistema. ¡Hasta pronto!':^{ANCHO}}")
        print()
        break

    # Pausa antes de volver al menú
    input("\n  Presiona Enter para volver al menú...")
