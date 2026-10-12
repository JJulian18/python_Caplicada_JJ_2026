# ==================================================================
#  p118-lote-autos.py
#  Diccionarios en Python - Parte 2 | Ejemplo 1: Lote de autos
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Sistema simple para controlar el inventario de un lote de autos:
#   - Almacenar los datos de cada vehiculo (marca, modelo, año).
#   - Usar una lista de diccionarios.
#   - Iniciar con algunos vehiculos precargados y permitir agregar
#     mas (captura hasta dejar la marca vacia).
#   - Imprimir un reporte del inventario completo en forma de
#     tabla y en forma de registro.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : marca, modelo y año de nuevos autos (marca vacia = fin).
#  Proceso : lista de diccionarios; append() para agregar;
#            autos[0].keys() para los encabezados; for anidado
#            sobre .values() (tabla) y .items() (registro).
#  Salida  : lista completa, total de autos, tabla y registros.
#  Ejemplo : 3 precargados (Mustang 1964, Jetta 2015, Focus 2000)
#            -> Total: 3
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Control de lote de autos (lista de diccionarios)")
print("-" * 60)

autos = [
    {'marca': 'Ford', 'modelo': 'Mustang', 'año': 1964},
    {'marca': 'VW', 'modelo': 'Jetta', 'año': 2015}
]
autos.append({'marca': 'Ford', 'modelo': 'Focus', 'año': 2000})

# Captura de autos adicionales
print("Captura de nuevos autos (deje la marca vacia para terminar)")
while True:
    marca = input("\nMarca ? ").strip()
    if marca == '':
        break
    modelo = input("Modelo ? ").strip()
    while True:
        try:
            anio = int(input("Año ? "))
            if 1886 <= anio <= 2030:
                break
            print("Error: el año debe estar entre 1886 y 2030.")
        except ValueError:
            print("Error: ingrese un año entero (ej. 2020).")
    autos.append({'marca': marca, 'modelo': modelo, 'año': anio})

print("\n" + "=" * 50)
print("Listado de Autos")
print("=" * 50)

print(f"\nTodos los autos : {autos} \nTotal: {len(autos)}")

print("\nCada auto dentro de los autos:")
print("-" * 50)
for auto in autos:
    print(auto)

print("\nDatos en forma de Tabla:")
print("-" * 50)
for k in autos[0].keys():
    print(f"{k:<12}", end="")
print("")
for auto in autos:
    for v in auto.values():
        print(f"{v:<12}", end="")
    print("")

print("\nDatos en forma de Registro")
print("-" * 50)
for auto in autos:
    for k, v in auto.items():
        print(f"{k:<12} : {v}")
    print("")
