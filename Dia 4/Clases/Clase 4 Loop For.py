# Loop For: El loop for es una estructura de control de flujo que se utiliza para iterar sobre una secuencia de elementos. En Python, el loop for se utiliza para recorrer
# una lista, una tupla, un diccionario, un conjunto o una cadena.

# Ejemplo de loop for en Python

# Ejemplo 1: recorrer una lista
frutas = ["manzana", "banana", "cereza"]
for x in frutas:
    print(x)

# Ejemplo 2: recorrer una cadena
for x in "banana":
    print(x)

# Ejemplo 3: recorrer un rango
for x in range(6):
    print(x)

# Ejemplo 4: recorrer un rango con un inicio y un final
for x in range(2, 6):
    print(x)

# Ejemplo 5: recorrer un rango con un inicio, un final y un paso de la iteración
for x in range(2, 30, 3):
    print(x)

# Ejemplo 6: recorrer un rango en orden inverso
for x in range(6, 2, -1):
    print(x)

# Ejemplo 7: recorrer un diccionario
frutas = {"manzana": 1, "banana": 2, "cereza": 3}
for x in frutas:
    print(x)

# Ejemplo 8: recorrer un diccionario con valores
frutas = {"manzana": 1, "banana": 2, "cereza": 3}
for x in frutas.values():
    print(x)

# Ejemplo 9: for a una lista con un strartswith
frutas = ["manzana", "banana", "cereza", "blueberry"]
for x in frutas:
    if x.startswith("b"):
        print(x)
    else:
        print("Nombres que no empiezan con b: ", x)
