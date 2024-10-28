# Los Sets: Son colecciones desordenadas de elementos únicos de la misma forma que los diccionarios, pero no tienen clave.
# Se utilizan para almacenar elementos que no se repiten.
# Se pueden definir con llaves {} o con la función set()
# Ejemplo:

# Crear un set
set1 = {1, 2, 3, 4, 5}
print(set1)
# Crear un set con la función set()
set2 = set([1, 2, 3, 4, 5])
print(set2)

# Los sets no permiten elementos duplicados
set3 = {1, 2, 3, 4, 5, 5}
print(set3)  # imprime {1, 2, 3, 4, 5}

# Los sets no permiten elementos mutables
# set4 = {1, 2, [3, 4], 5}  # Error

# Los sets no permiten indexación
# print(set1[0])  # Error

# Los sets no permiten slicing
# print(set1[0:2]) # Error

# Los sets no permiten elementos mutables
# set4 = {1, 2, [3, 4], 5} # Error

# Si aceptan elementos inmutables
set5 = {1, 2, (3, 4), 5}
print(set5)

# Se puede medir la longitud de un set
print(len(set1))

# Se puede verificar si un elemento está en un set
print(1 in set1)  # imprime True
print(6 in set1)  # imprime False

# Se puede agregar un elemento a un set
set1.add(6)
print(set1)  # imprime {1, 2, 3, 4, 5, 6}

# Se puede agregar varios elementos a un set
set1.update([7, 8, 9])
print(set1)  # imprime {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Se puede eliminar un elemento de un set
set1.remove(9)
print(set1)  # imprime {1, 2, 3, 4, 5, 6, 7, 8}

# Se puede eliminar un elemento de un set con discard
set1.discard(8)
print(set1)  # imprime {1, 2, 3, 4, 5, 6, 7}
# Diferencia entre remove y discard de la función remove si el elemento no existe en el set se genera un error y con discard no.

# Se puede eliminar un elemento de un set con pop
set1.pop()
print(set1)  # imprime {2, 3, 4, 5, 6, 7}

# Se puede vaciar un set
set1.clear()
print(set1)  # imprime set()

# Se puede unir dos sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}

set3 = set1.union(set2)
print(set3)  # imprime {1, 2, 3, 4, 5, 6}

# Se puede unir dos sets con el método update
set1.update(set2)
print(set1)  # imprime {1, 2, 3, 4, 5, 6}
