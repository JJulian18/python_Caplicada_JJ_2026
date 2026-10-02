# ==================================================================
#  p103-resumen-ventas.py
#  Listas en Python - Parte 3 | Ejemplo 6: Resumen de ventas
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Procesar ventas diarias:
#   - Aplicar un descuento del 10% a los importes mayores de $1,000.
#   - Conservar los demas importes sin cambios.
#   - Crear otra lista con las ventas finales mayores de $500.
#   - Mostrar los resultados redondeados a dos decimales.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : lista fija de ventas.
#  Proceso : comprension con expresion condicional (descuento) y
#            comprension con filtro (ventas > 500); sum() para total.
#  Salida  : ventas originales, finales, relevantes y su total.
#  Ejemplo : 1200 -> 1080.0 ; 1800 -> 1620.0
# ==================================================================

print("\033[2J\033[H", end="", flush=True)
print("Resumen de ventas")
print("-" * 60)

ventas = [250, 800, 1200, 450, 1800, 950]

finales = [round(v * 0.90, 2) if v > 1000 else v
           for v in ventas]

relevantes = [v for v in finales if v > 500]

print(f"Ventas originales     : {ventas}")
print(f"Ventas finales        : {finales}")
print(f"Ventas mayores de $500: {relevantes}")
print(f"Total relevante       : ${sum(relevantes):,.2f}")
