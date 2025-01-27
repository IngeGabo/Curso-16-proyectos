# Esta clase es de trucos para listas, como agregar elementos, eliminar elementos, contar elementos, etc.

# Crear una lista de una palabra

palabra = "PALABRA"
lista = [letra for letra in palabra]
print(lista)

# Crear una lista de números

numeros = [numero for numero in range(1, 50, 2)]
print(numeros)

# Crear una lista de números porcentaje

porcentaje = [par/100 for par in range(1, 100)]
print(porcentaje)

# Crear una lista de números con un if

pares = [par for par in range(1, 100) if par % 2 == 0]
print(pares)

# Crear una lista de números con un if y un else

pares = [par if par % 2 == 0 else "Impar" for par in range(1, 100)]
print(pares)

# Ejemplo util

pies = [10, 20, 30, 40, 50]
metros = [pie*0.3048 for pie in pies]
print(metros)
