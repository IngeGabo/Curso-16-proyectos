# Las propiedades del String:
# - Inmutabilidad
# - Concatenación
# - Indexación
# - Multilineales
# - Verificación de contenido
# - Calcular longitud

# Inmutabilidad
# nombre = "Carina"
# nombre[0] = "K"
# print(nombre)
# Esto nos arrojará un error, ya que los strings son inmutables, es decir, no se pueden modificar una vez creados. Si queremos cambiar un string, debemos crear uno nuevo.

nombre = "Carina"
nombre = "Karina"
print(nombre)

# Concatenación
numb1 = "Kari"
numb2 = "na"
print(numb1 + numb2)
print(numb1 * 10)

# Multilineales
# Podemos crear strings multilineales con triple comillas simples o dobles.
poema = """En la calle codo a codo de la mano
Va el poeta con el pueblo
Siempre sueña el alba
Siempre sueña el hombre"""
print(poema)

# Verificación de contenido
print("poeta" in poema)  # True
print("perro" in poema)  # False

# Calcular longitud
print(len(poema))  # 97
