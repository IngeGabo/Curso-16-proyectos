# El Formateo de Cadenas es una técnica que permite crear cadenas de texto con valores de variables de una
# forma más sencilla y legible.

color = "rojo"
matricula = 1234

# El formateo de cadenas se puede realizar de las siguientes formas:
# 1. Utilizando el operador %.
# Ejemplo 1 de formateo de cadenas
print("El color del auto es %s y la matrícula es %d" % (color, matricula))
# 2. Utilizando el método format().
# Ejemplo 2 de formateo de cadenas
print("El color del auto es {} y la matrícula es {}".format(color, matricula))
# 3. Utilizando f-strings. (Python 3.6+) El método más sencillo y recomendado.
# Ejemplo 3 de formateo de cadenas
print(f"El color del auto es {color} y la matrícula es {matricula}")
