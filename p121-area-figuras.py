# ==================================================================
#  p121-area-figuras.py
#  Diccionarios en Python - Parte 2 | Ejemplo 4: Area figuras
# ------------------------------------------------------------------
#  PLANTEAMIENTO
#  Calculadora geometrica dinamica:
#   - Almacenar la informacion de varias figuras (Circulo,
#     Triangulo, Rectangulo) en un diccionario de diccionarios.
#   - Para cada figura guardar sus parametros (ej. "radio") y la
#     formula de su area como un string.
#   - El usuario elige una figura y captura los datos necesarios.
#   - Calcular y mostrar el area interpretando la formula
#     almacenada.
# ------------------------------------------------------------------
#  ANALISIS
#  Entrada : nombre de la figura (validado con in) y sus medidas
#            (numeros positivos).
#  Proceso : diccionario de diccionarios figuras; for sobre
#            .items() para mostrar el menu; acceso
#            figuras[fig]['formula']; replace() de las variables
#            por sus valores y eval() para evaluar la formula.
#  Salida  : area de la figura con 4 decimales.
#  Ejemplo : Circulo r=2 -> 12.5664 ; Triangulo b=4 a=3 -> 6.0000 ;
#            Rectangulo l=5 a=2 -> 10.0000
# ==================================================================

import math

print("\033[2J\033[H", end="", flush=True)
print("Área de Figuras Geométricas")
print("-" * 60)

figuras = {
    "Circulo": {"radio": 0, "formula": "math.pi * r ** 2"},
    "Triangulo": {"base": 0, "altura": 0, "formula": "0.5 * b * a"},
    "Rectangulo": {"largo": 0, "ancho": 0, "formula": "l * a"}
}


def pedir_medida(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Error: la medida debe ser un numero positivo.")
        except ValueError:
            print("Error: ingrese un numero (ej. 4.5).")


print("Calculadora de áreas de figuras geométricas")
print("Figuras disponibles:")
for k, v in figuras.items():
    print(f"{k:<10} - Fórmula: {v['formula']}")

while True:
    fig = input("\nElige una Figura: ").strip().title()
    if fig in figuras:
        break
    print("Error: Figura no válida. Intenta de nuevo.")

area = 0
if fig == 'Circulo':
    r = pedir_medida('Radio  : ')
    figuras[fig]['radio'] = r
    area = eval(figuras[fig]['formula'].replace('r', str(r)))
elif fig == 'Triangulo':
    b = pedir_medida('Base   : ')
    a = pedir_medida('Altura : ')
    figuras[fig]['base'] = b
    figuras[fig]['altura'] = a
    formula_lista = figuras[fig]['formula'].replace('b', str(b)).replace('a', str(a))
    area = eval(formula_lista)
elif fig == 'Rectangulo':
    l = pedir_medida('Largo  : ')
    a = pedir_medida('Ancho  : ')
    figuras[fig]['largo'] = l
    figuras[fig]['ancho'] = a
    formula_lista = figuras[fig]['formula'].replace('l', str(l)).replace('a', str(a))
    area = eval(formula_lista)

print(f"\nDatos de la figura: {figuras[fig]}")
print(f"El Área del {fig} es : {area:.4f}")
