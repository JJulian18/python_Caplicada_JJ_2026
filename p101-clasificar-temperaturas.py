# ==================================================================
#  p101-clasificar-temperaturas.py
#  Listas en Python - Parte 3 | Ejemplo 4: Clasificar temperaturas
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Dada una lista de temperaturas en grados Celsius, crear una nueva
#  lista de etiquetas:
#   - Menor de 15           -> "Fria"
#   - Entre 15 y 25 (incl.) -> "Templada"
#   - Mayor de 25           -> "Caliente"
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista fija de temperaturas (°C).
#  Proceso : comprension con expresion condicional encadenada
#            (valor_si if cond else valor_si2 if cond2 else valor_no).
#  Salida  : temperaturas y su clasificacion.
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Clasificar temperaturas")
print("-" * 60)

temperaturas = [8, 14, 18, 22, 27, 35]

clasificacion = [
    "Fría" if t < 15 else
    "Templada" if t <= 25 else
    "Caliente"
    for t in temperaturas
]

print(f"Temperaturas : {temperaturas}")
print(f"Clasificacion: {clasificacion}\n")

# Detalle por temperatura (ciclo tradicional: solo para imprimir)
for t, etiqueta in zip(temperaturas, clasificacion):
    print(f"{t:>4} °C -> {etiqueta}")
