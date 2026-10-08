# ==================================================================
#  p113-calificaciones-estudiante.py
#  Diccionarios en Python - Parte 1 | Ejemplo 2: Calificaciones
#  estudiante
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Procesar las calificaciones de un estudiante en un semestre:
#   - Crear dos listas: materias y calificaciones.
#   - Combinar ambas listas en un diccionario y mostrarlo.
#   - Agregar, eliminar y actualizar elementos del diccionario.
#   - Iterar el diccionario final mostrando materia y calificacion,
#     y calcular la suma total y el promedio.
#   - Vaciar completamente el diccionario.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : listas fijas de materias y calificaciones.
#  Proceso : dict(zip()) para crear; update() para agregar y
#            modificar; pop() y popitem() para eliminar; for sobre
#            .items() acumulando la suma; clear() para vaciar.
#  Salida  : diccionario en cada etapa, listado final, suma y
#            promedio.
#  Ejemplo : finales Quimica 10, Matematicas 10, Geografia 7.5,
#            Estadistica 6, Ingles 10 -> suma 43.5, promedio 8.70
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Gestion de calificaciones de un estudiante")
print("-" * 60)

materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = [10, 9, 8, 7.5, 6]
print(f"Lista de materias:\n{materias}\n")
print(f"Lista de calificaciones:\n{califs}")

# Crear el diccionario juntando las dos listas
notas = dict(zip(materias, califs))
print(f"\nDiccionario nuevo juntando las listas:\n{len(notas)} - {notas}")

# Agregar elementos
notas.update({'Ingles': 10})
notas.update({'Programacion': 7})
print(f"\nSe agregaron elementos:\n{len(notas)} - {notas}")

# Remover elementos: por llave y el ultimo insertado
notas.pop('Fisica')
notas.popitem()
print(f"\nSe removieron elementos:\n{len(notas)} - {notas}")

# Modificar elementos existentes
notas.update({'Quimica': 10})
notas.update({'Matematicas': 10})
print(f"\nSe modificaron elementos:\n{len(notas)} - {notas}")

s = 0
print("\nMaterias y calificaciones finales:\n")
for m, c in notas.items():
    print(f"{m:<12} - {c:5}")
    s += c

p = s / len(notas)
print(f"\nLa suma: {s} y el promedio: {p:.2f}")

notas.clear()
print(f"\nSe borro todo: {notas}")
