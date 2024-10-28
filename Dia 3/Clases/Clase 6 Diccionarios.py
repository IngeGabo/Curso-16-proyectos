# Diccionarios(Diccionary): El diccionario es una estructura de datos que permite almacenar un conjunto de pares clave-valor, donde cada clave es única.
# Para crear un diccionario, utilizamos llaves {} y separamos los pares clave-valor con comas. Por ejemplo:

diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}
# imprime {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}
print(diccionario)

# Podemos acceder a los valores de un diccionario utilizando su clave. Por ejemplo, para acceder al valor asociado a la clave "nombre".
print(diccionario["nombre"])  # imprime Juan

# Podemos modificar los valores de un diccionario utilizando su clave. Por ejemplo, para modificar el valor asociado a la clave "edad".
diccionario["edad"] = 30
# imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Bogotá'}
print(diccionario)

# Podemos agregar nuevos pares clave-valor a un diccionario. Por ejemplo, para agregar la clave "profesión" con el valor "Ingeniero".
diccionario["profesión"] = "Ingeniero"
# imprime {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Bogotá', 'profesión': 'Ingeniero'}
print(diccionario)

# Podemos utilizar el método pop() para eliminar un par clave-valor de un diccionario. Por ejemplo, para eliminar la clave "ciudad" y su valor asociado.
diccionario.pop("ciudad")
# imprime {'nombre': 'Juan', 'edad': 30, 'profesión': 'Ingeniero'}
print(diccionario)

# Podemos obtener las claves de un diccionario utilizando el método keys(). Por ejemplo, para obtener las claves del diccionario.
print(diccionario.keys())  # print dict_keys(['nombre', 'edad', 'profesión'])

# Podemos obtener los valores de un diccionario utilizando el método values(). Por ejemplo, para obtener los valores del diccionario.
print(diccionario.values())  # print dict_values(['Juan', 30, 'Ingeniero'])

# Podemos obtener los pares clave-valor de un diccionario utilizando el método items(). Por ejemplo, para obtener los pares clave-valor del diccionario.
# print dict_items([('nombre', 'Juan'), ('edad', 30), ('profesión', 'Ingeniero')])
print(diccionario.items())

# Podemos utilizar el operador in para verificar si una clave se encuentra en un diccionario. Por ejemplo, para verificar si la clave "nombre" se encuentra en el diccionario.
print("nombre" in diccionario)  # imprime True
print("ciudad" in diccionario)  # imprime False

# Podemos utilizar el operador not in para verificar si una clave no se encuentra en un diccionario. Por ejemplo, para verificar si la clave "ciudad" no se encuentra en el diccionario.
print("ciudad" not in diccionario)  # imprime True
print("nombre" not in diccionario)  # imprime False

# Podemos utilizar el método clear() para eliminar todos los pares clave-valor de un diccionario. Por ejemplo, para eliminar todos los pares clave-valor del diccionario.
diccionario.clear()
print(diccionario)  # imprime {}

# Podemos utilizar el método copy() para crear una copia de un diccionario. Por ejemplo, para crear una copia del diccionario.
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Bogotá"}
diccionarioCopia = diccionario.copy()
# imprime {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}
print(diccionarioCopia)

# Podemos utilizar el método update() para combinar dos diccionarios. Por ejemplo, para combinar el diccionario con otro diccionario.
diccionario2 = {"profesión": "Ingeniero", "ciudad": "Medellín"}
diccionario.update(diccionario2)
print(diccionario)
# imprime {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Medellín', 'profesión': 'Ingeniero'}, si ambos tienen un valor en ciuudades, se reemplaza el valor de la primera por el de la segunda

# Podemos utilizar el método get() para obtener el valor asociado a una clave en un diccionario. Por ejemplo, para obtener el valor asociado a la clave "nombre".
print(diccionario.get("nombre"))  # imprime Juan

# Si la clave no se encuentra en el diccionario, el método get() devuelve None. Por ejemplo, para obtener el valor asociado a la clave "apellido".
print(diccionario.get("apellido"))  # imprime None

# Podemos especificar un valor predeterminado para el método get(). Por ejemplo, para obtener el valor asociado a la clave "apellido" con un valor predeterminado de "Pérez".
print(diccionario.get("apellido", "Pérez"))  # imprime Pérez

# Podemos tener listas dentro de diccionarios. Por ejemplo, para crear un diccionario con una lista de números.
diccionario = {"tema": "numeros", "números": [1, 2, 3, 4, 5]}
# imprimir el 3
print(diccionario["números"][2])

# Podemos tener diccionarios dentro de diccionarios. Por ejemplo, para crear un diccionario con otro diccionario.
diccionario = {"tema": "diccionarios",
               "diccionario": {"nombre": "Juan", "edad": 25}}
# imprimir Juan
print(diccionario["diccionario"]["nombre"])
