# Tuples(tuplas): Tuples son una colección ordenada e inmutable. Permite duplicados.
# Las tuplas se escriben con paréntesis. El tuplas no se puede cambiar, agregar o eliminar elementos después de la creación.
# Ejemplo de tupla:

tupla = ("manzana", "banana", "cereza")
print(tupla)

# Acceder a los elementos de una tupla:
# Se puede acceder a los elementos de la tupla haciendo referencia al número de índice, dentro de corchetes.

print(tupla[1])

# Recorrer una tupla:

for fruta in tupla:
    print(fruta)

# Longitud de una tupla:

print(len(tupla))

# Crear una tupla con un solo elemento:
# Para crear una tupla con un solo elemento, debe agregar una coma después del elemento, de lo contrario Python no lo reconocerá como una tupla.

tupla = ("manzana",)
print(type(tupla))

# No se puede cambiar el valor de una tupla:
# Una vez que se ha creado una tupla, no puede cambiar sus valores. Las tuplas son inmutables.

# tupla[1] = "naranja" # Esto generará un error

# Eliminar una tupla:
# Como las tuplas son inmutables, no se pueden eliminar elementos individuales en tuplas. Pero se puede eliminar la tupla completa.


# Ejemplos de tuplas:
tuplasNumero = (1, 2, 3, 4, 5)
tuplasMixta = (1, "hola", 3.14, True)
tuplasAnidadas = (1, (2, 3, 4), (5, 6, 7))
tuplasVacia = ()
tuplasUnElemento = (1,)
tuplasBoolean = (True, False, True)
tuplasString = ("Hola", "Mundo", "Python")
tuplasLista = ([1, 2, 3], [4, 5, 6], [7, 8, 9])


# Convertir de una lista a una tupla:
# Se puede convertir una lista en una tupla utilizando la función tuple().
# Ejemplo:

lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(tupla)

# Convertir de una tupla a una lista:
# Se puede convertir una tupla en una lista utilizando la función list().
# Ejemplo:

tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
print(lista)


# Desempaquetado de tuplas:
# Cuando se crea una tupla, los elementos se colocan entre paréntesis. Pero cuando se asigna una tupla a variables, los elementos de la tupla se pueden "desempaquetar" en
# variables individuales.

tupla = ("manzana", "banana", "cereza")
(a, b, c) = tupla
print(a)
print(b)
print(c)

# Metodo count():
# Este método devuelve el número de veces que un valor específico aparece en la tupla.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
print(tupla.count(1))

# Metodo index():
# Este método busca en la tupla un valor específico y devuelve la posición de donde se encontró.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
print(tupla.index(5))
