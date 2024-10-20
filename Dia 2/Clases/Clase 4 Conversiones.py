# Conversiones de tipos de datos
# Convertir un tipo de dato a otro, es cuando se toma un valor de un tipo de dato y se convierte a otro tipo de dato.

# Para convertir un tipo de dato a otro, se utilizan las funciones int(), float(), str() y bool().

# Ejemplo 1 de conversiones de tipos de datos
# Convertir un valor de tipo entero a tipo flotante
x = 10
y = float(x)
print(y)

# Ejemplo 2 de conversiones de tipos de datos
# Convertir un valor de tipo flotante a tipo entero
x = 10.5
y = int(x)
print(y)

# Ejemplo 3 de conversiones de tipos de datos
# Convertir un valor de tipo entero a tipo cadena
x = 10
y = str(x)
print(y)
print(type(y))

# Ejemplo 4 de conversiones de tipos de datos
# Convertir un valor de tipo cadena a tipo entero
x = "10"
y = int(x)
print(y)
print(type(y))

# Ejemplo 5 de conversiones de tipos de datos
# Convertir un valor de tipo cadena a tipo flotante
x = "10.5"
y = float(x)
print(y)
print(type(y))

# Ejemplo 6 de conversiones de tipos de datos
# Convertir un valor de tipo flotante a tipo cadena
x = 10.5
y = str(x)
print(y)
print(type(y))

# Ejemplo 7 de conversiones de tipos de datos
# Convertir un valor de tipo entero a tipo booleano
x = 10  # True si el valor es diferente de 0, False si el valor es 0
y = bool(x)
print(y)
print(type(y))

# El uso del input() para obtener datos del usuario y la conversión de tipos de datos
edad = input("Ingrese su edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = edad + 1
print("Su nueva edad es:", nueva_edad)
