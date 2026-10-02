# ==================================================================
#  p100-normalizar-nombres.py
#  Listas en Python - Parte 3 | Ejemplo 3: Normalizar nombres
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Limpiar una lista de nombres escritos con espacios sobrantes y
#  combinaciones de mayusculas y minusculas:
#   - Eliminar los espacios sobrantes.
#   - Convertir cada nombre a formato de titulo.
#   - Descartar las entradas vacias.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista fija de nombres.
#  Proceso : comprension que transforma (strip().title()) y filtra
#            (if nombre.strip()) en una sola expresion.
#  Salida  : datos originales y nombres normalizados.
#  Nota    : la lista original no cambia; se crea una lista nueva.
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Normalizar nombres")
print("-" * 60)

nombres = [" ana", "LUIS ", "", " maría josé ", "Pedro"]

normalizados = [nombre.strip().title() for nombre in nombres if nombre.strip()]

print(f"Datos originales    : {nombres}")
print(f"Nombres normalizados: {normalizados}")
print(f"Entradas descartadas: {len(nombres) - len(normalizados)}")
