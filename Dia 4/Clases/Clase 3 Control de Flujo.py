# El control de flujo es el control de la ejecución de un programa. En Python, el control de flujo se logra mediante el uso de estructuras de control de flujo,
# como las declaraciones if, elif y else. Estas declaraciones permiten que un programa ejecute diferentes bloques de código según una condición dada.


# Ejemplo de declaración if
# La declaración if se utiliza para ejecutar un bloque de código si una condición es verdadera. Aquí hay un ejemplo de una declaración if en Python:

# Ejemplo 1: el bloque de código se ejecutará si la condición es verdadera
if 5 > 2:
    print("5 es mayor que 2")

# Ejemplo 2: el bloque de código siempre se ejecutará
if True:
    print("Esta declaración siempre se ejecutará")

# If Else
# La declaración if else se utiliza para ejecutar un bloque de código si la condición es verdadera y otro bloque de código si la condición es falsa.
# Aquí hay un ejemplo de una declaración if else en Python:

# Ejemplo 1: el bloque de código se ejecutará si la condición es verdadera
if 5 > 2:
    print("5 es mayor que 2")
else:
    print("5 no es mayor que 2")

# Ejemplo 2: el bloque de código se ejecutará si la condición es falsa
if 5 < 2:
    print("5 es menor que 2")
else:
    print("5 no es menor que 2")

# If Elif Else
# La declaración if elif else se utiliza para ejecutar diferentes bloques de código según diferentes condiciones.
# Aquí hay un ejemplo de una declaración if elif else en Python:

# Ejemplo 1: el bloque de código se ejecutará si la primera condición es verdadera
if 5 > 2:
    print("5 es mayor que 2")
elif 5 == 2:
    print("5 es igual a 2")
else:
    print("5 no es mayor que 2 y 5 no es igual a 2")

# Ejemplo 2: el bloque de código se ejecutará si la segunda condición es verdadera
if 5 < 2:
    print("5 es menor que 2")
elif 5 == 2:
    print("5 es igual a 2")
else:
    print("5 no es menor que 2 y 5 no es igual a 2")

# If anidado
# Los bloques de código dentro de una declaración if, elif o else pueden contener otras declaraciones if, elif o else.

# Ejemplo de declaración if anidada
x = 41

if x > 10:
    print("x es mayor que 10")
    if x > 20:
        print("x es también mayor que 20")
    else:
        print("x es menor que 20")
