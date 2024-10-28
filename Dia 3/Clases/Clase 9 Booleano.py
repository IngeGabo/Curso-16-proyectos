# Los booleanos(boolean) son un tipo de dato que puede tener dos valores: True o False.
# Se pueden contruir de diferentes maneras:

# 1. Asignando directamente el valor booleano:

mi_booleano = True
print(mi_booleano)  # True

mi_booleano = False
print(mi_booleano)  # False

# 2. Usando el constructor bool():

mi_booleano = bool(1)
print(mi_booleano)  # True

mi_booleano = bool(0)
print(mi_booleano)  # False

# 3. Usando el constructor bool() con un string:

mi_booleano = bool("Hola")
print(mi_booleano)  # True

mi_booleano = bool("")
print(mi_booleano)  # False

# 4. Usando el constructor bool() con una lista:

mi_booleano = bool([1, 2, 3])
print(mi_booleano)  # True

mi_booleano = bool([])
print(mi_booleano)  # False

# Con mayor y menor que:

mi_booleano = 5 > 3
print(mi_booleano)  # True

mi_booleano = 5 < 3
print(mi_booleano)  # False

# Con igualdad:

mi_booleano = 5 == 5
print(mi_booleano)  # True

mi_booleano = 5 == 3
print(mi_booleano)  # False

# Con desigualdad:

mi_booleano = 5 != 3
print(mi_booleano)  # True

mi_booleano = 5 != 5
print(mi_booleano)  # False

# Con mayor o igual que:

mi_booleano = 5 >= 3
print(mi_booleano)  # True

mi_booleano = 5 >= 5
print(mi_booleano)  # True

mi_booleano = 5 >= 7
print(mi_booleano)  # False
