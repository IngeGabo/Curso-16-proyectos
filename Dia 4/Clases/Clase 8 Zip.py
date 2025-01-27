# Funcion Zip: La función Zip para unir dos listas en una sola lista de tuplas de la forma (a,b)

# Ejemplo 1:
a = [1, 2, 3]
b = [4, 5, 6]
c = zip(a, b)
print(list(c))

# Ejemplo 2: Funionalidad en la vida real
nombres = ['Juan', 'Pedro', 'Maria']
edades = [20, 30, 40]
personas = zip(nombres, edades)
print(list(personas))

# Ejemplo 3: Unir tres listas
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = zip(a, b, c)
print(list(d))

# Ejemplo 4: Unir dos listas de diferentes tamaños
a = [1, 2, 3]
b = [4, 5]
c = zip(a, b)
print(list(c))

# Nota: como se puede observar, la función zip une las listas hasta el tamaño de la lista más pequeña, los terminos de la lista más grande se ignoran.

# Ejemplo 5: Imprimiendo los elementos de la lista
nombres = ['Juan', 'Pedro', 'Maria']
edades = [20, 30, 40]
personas = zip(nombres, edades)
for nombre, edad in personas:
    print(nombre, edad)

# Ejemplo 6: Usando la función zip con un diccionario
nombres = ['Juan', 'Pedro', 'Maria']
edades = [20, 30, 40]
personas = dict(zip(nombres, edades))
print(personas)
