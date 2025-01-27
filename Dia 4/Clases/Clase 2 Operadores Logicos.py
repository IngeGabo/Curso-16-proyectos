# Los Operadores Logicos sirven como conectores para unir o cambiar la logica de las expresiones
# Los operadores logicos son: and, or, not

# Operador and
# El operador and devuelve True si ambas expresiones son verdaderas
# Ejemplo
x = 5
print(x > 3 and x < 10)  # True

# Tabla de verdad del operador and
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# Operador or
# El operador or devuelve True si al menos una de las expresiones es verdadera
# Ejemplo
x = 5
print(x > 3 or x < 4)  # True

# Tabla de verdad del operador or
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# Operador not
# El operador not devuelve False si la expresion es verdadera y True si la expresion es falsa
# Ejemplo
x = 5
print(not (x > 3 and x < 10))  # False

# Tabla de verdad del operador not
# not True = False
# not False = True

# Como buenas practicas se recomienda usar parentesis para hacer mas legible el codigo
# Ejemplo
x = 5
print((x > 3) and (x < 10))  # True
print((x > 3) or (x < 4))  # True
print(not (x > 3 and x < 10))  # False

# Busca de texto con operadores logicos
# Ejemplo
texto = "Hola Mundo"
print("Hola" in texto and "Mundo" in texto)  # True
