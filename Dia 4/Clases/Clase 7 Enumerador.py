# Enumerador: Range en una función, que permite recorrer una lista de valores, por ejemplo, de 0 a 10.

lista = range(0, 10)
for i in lista:
    print(i)

# Cosas que tines que considerar al usar esta función:
# 1. El primer valor es el valor inicial.
# 2. El segundo valor es el valor final, pero no se incluye en la lista.
# 3. Si solo se coloca un valor, se asume que es el valor final y el inicial es 0.
# 4. Si se coloca un tercer valor, este es el incremento.
# 5. El incremento puede ser negativo.
# 6. El incremento no puede ser 0.

# Ejemplo de el primer valor es el valor inicial.
lista = range(10)
for i in lista:
    print(i)

# Ejemplo de el incremento.
lista = range(0, 10, 2)
for i in lista:
    print(i)

# Ejemplo de el incremento negativo.
lista = range(10, 0, -1)
for i in lista:
    print(i)

# Si quieres crear una lista de valores, puedes convertir el rango en una lista.
lista = list(range(0, 10))
print(lista)
