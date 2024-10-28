# Listas(list): Las listas son un tipo de dato que nos permite almacenar distintos valores, sean estos números, strings, booleanos, etc. Las listas son mutables,
# es decir, podemos modificarlas una vez que han sido creadas. Para crear una lista, utilizamos corchetes [] y separamos los elementos con comas. Por ejemplo:

listaDeNumeros = [1, 2, 3, 4, 5]
listaDeFloats = [3.14, 2.71, 1.61]
listaDeStrings = ["Hola", "Mundo", "Python"]
listaDeBooleanos = [True, False, True, True]
listaMixta = [1, "Hola", True, 3.14]

# Podemos acceder a los elementos de una lista utilizando su índice. Los índices en Python comienzan en 0. Por ejemplo, para acceder al primer elemento de la listaDeNumeros.
print(listaDeNumeros[0])

# Para acceder al último elemento de una lista, podemos utilizar índices negativos. Por ejemplo, para acceder al último elemento de la listaDeNumeros.
print(listaDeNumeros[-1])

# Podemos modificar los elementos de una lista utilizando su índice. Por ejemplo, para modificar el primer elemento de la listaDeNumeros.
listaDeNumeros[0] = 100

# Podemos agregar elementos a una lista utilizando el método append(). Por ejemplo, para agregar el número 6 a la listaDeNumeros.
listaDeNumeros.append(6)
print(listaDeNumeros)  # el listaDeNumeros ahora es [100, 2, 3, 4, 5, 6]

# Podemos utilizar el método remove() para eliminar la primera aparición de un elemento en una lista. Por ejemplo, para eliminar la primera aparición del número 2 en la listaDeNumeros.
listaDeNumeros.remove(2)
print(listaDeNumeros)  # el listaDeNumeros ahora es [100, 3, 4, 5, 6]

# Podemos obtener el largo de una lista utilizando la función len(). Por ejemplo, para obtener el largo de la listaDeNumeros.
print(len(listaDeNumeros))  # imprime 5
print(len(listaDeBooleanos))  # imprime 4

# Podemos concatenar listas utilizando el operador +. Por ejemplo, para concatenar la listaDeNumeros con la listaDeFloats.
listaConcatenada = listaDeNumeros + listaDeFloats
print(listaConcatenada)  # imprime [100, 3, 4, 5, 6, 3.14, 2.71, 1.61]

# Podemos crear listas anidadas, es decir, listas que contienen otras listas. Por ejemplo, para crear una lista que contenga la listaDeNumeros y la listaDeFloats.
listaAnidada = [listaDeNumeros, listaDeFloats]
print(listaAnidada)  # imprime [[100, 3, 4, 5, 6], [3.14, 2.71, 1.61]]

# Podemos acceder a los elementos de una lista anidada utilizando múltiples índices. Por ejemplo, para acceder al primer elemento de la listaDeNumeros dentro de la listaAnidada.
print(listaAnidada[0][0])  # imprime 100
print(listaAnidada[0][1])  # imprime 3
print(listaAnidada[1][0])  # imprime 3.14
print(listaAnidada[1][1])  # imprime 2.71

# Podemos utilizar el operador in para verificar si un elemento se encuentra en una lista. Por ejemplo, para verificar si el número 100 se encuentra en la listaDeNumeros.
print(100 in listaDeNumeros)  # imprime True
print(200 in listaDeNumeros)  # imprime False

# Podemos utilizar el operador not in para verificar si un elemento no se encuentra en una lista. Por ejemplo, para verificar si el número 200 no se encuentra en la listaDeNumeros.
print(200 not in listaDeNumeros)  # imprime True
print(100 not in listaDeNumeros)  # imprime False

# Podemos utilizar el operador * para repetir los elementos de una lista. Por ejemplo, para repetir la listaDeNumeros 3 veces.
# imprime [100, 3, 4, 5, 6, 100, 3, 4, 5, 6, 100, 3, 4, 5, 6]
print(listaDeNumeros * 3)

# Podemos utilizar el método sort() para ordenar los elementos de una lista. Por ejemplo, para ordenar la listaDeNumeros de forma ascendente.
listaDeNumeros.sort()
print(listaDeNumeros)  # imprime [3, 4, 5, 6, 100]

# Podemos utilizar el método reverse() para invertir el orden de los elementos de una lista. Por ejemplo, para invertir el orden de la listaDeNumeros.
listaDeNumeros.reverse()
print(listaDeNumeros)  # imprime [100, 6, 5, 4, 3]

# Podemos utilizar el método clear() para eliminar todos los elementos de una lista. Por ejemplo, para eliminar todos los elementos de la listaDeNumeros.
listaDeNumeros.clear()
print(listaDeNumeros)  # imprime []

# Podemos utilizar el método copy() para copiar una lista. Por ejemplo, para copiar la listaDeFloats en una nueva lista llamada listaDeFloatsCopia.
listaDeFloatsCopia = listaDeFloats.copy()
print(listaDeFloatsCopia)  # imprime [3.14, 2.71, 1.61]

# Podemos utilizar el método count() para contar cuántas veces aparece un elemento en una lista. Por ejemplo, para contar cuántas veces aparece el número 3 en la listaDeNumeros.
listaDeNumeros = [1, 2, 3, 4, 5, 3, 3, 3]
print(listaDeNumeros.count(3))  # imprime 4

# Podemos utilizar el método index() para obtener el índice de la primera aparición de un elemento en una lista. Por ejemplo, para obtener el índice del número 3 en la listaDeNumeros.
print(listaDeNumeros.index(3))  # imprime 2

# Podemos utilizar el método insert() para insertar un elemento en una lista en una posición específica. Por ejemplo, para insertar el número 100 en la posición 0 de la listaDeNumeros.
listaDeNumeros.insert(0, 100)
print(listaDeNumeros)  # imprime [100, 1, 2, 3, 4, 5, 3, 3, 3]

# Podemos utilizar el método pop() para eliminar un elemento de una lista en una posición específica. Por ejemplo, para eliminar el elemento en la posición 0 de la listaDeNumeros.
eliminado = listaDeNumeros.pop(0)
print(eliminado)  # imprime 100
print(listaDeNumeros)  # imprime [1, 2, 3, 4, 5, 3, 3, 3]

# Podemos utilizar el método extend() para agregar los elementos de una lista a otra lista. Por ejemplo, para agregar los elementos de la listaDeFloats a la listaDeNumeros.
listaDeNumeros.extend(listaDeFloats)
print(listaDeNumeros)  # imprime [1, 2, 3, 4, 5, 3, 3, 3, 3.14, 2.71, 1.61]
