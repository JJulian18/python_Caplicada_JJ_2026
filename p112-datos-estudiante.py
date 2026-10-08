# ==================================================================
#  p112-datos-estudiante.py
#  Diccionarios en Python - Parte 1 | Ejemplo 1: Datos estudiante
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Gestionar la informacion de un estudiante usando un diccionario:
#   - Inicializar: crear el diccionario con nombre, edad, email y
#     carrera.
#   - Actualizar: modificar el email y agregar la llave calificacion.
#   - Reportar: imprimir el diccionario completo actualizado.
#   - Desglosar: mostrar las llaves, los valores y un listado
#     formateado llave: valor.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : diccionario fijo con los datos del estudiante.
#  Proceso : asignacion por llave (modificar y agregar); for sobre
#            .keys(), .values() e .items().
#  Salida  : diccionario original, actualizado, llaves, valores y
#            listado llave : valor.
#  Ejemplo : email 'jperez@msn.com' -> 'juanp@gmail.com',
#            se agrega calificacion : 9.5
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Gestion de datos de estudiantes")
print("-" * 60)

estudiante = {
    'nombre': 'Juan Perez',
    'edad': 45,
    'email': 'jperez@msn.com',
    'carrera': 'Sistemas'
}
print(f"\nEl diccionario original:\n\n{estudiante}")

# Actualizar: modificar una llave existente y agregar una nueva
estudiante['calificacion'] = 9.5
estudiante['email'] = 'juanp@gmail.com'
print(f"\nEl diccionario actualizado:\n\n{estudiante}")

print("\nLas llaves del diccionario:\n")
for k in estudiante.keys():
    print(k)

print("\nLos valores del diccionario:\n")
for v in estudiante.values():
    print(v)

print("\nListado de llaves y valores:\n")
for k, v in estudiante.items():
    print(f"{k:<12} : {v}")
