# Random es una librería que nos permite generar números aleatorios, para ello debemos importarla.
from random import *

# randint(a, b) nos permite generar un número aleatorio entre a y b.
print(randint(1, 10))

# Podemos generar un número aleatorio entre 0 y 1.
print(randint(0, 1))

# Podemos generar un número aleatorio entre 0 y 100.
print(randint(0, 100))

# uniform es una número aleatorio entre a y b, pero puede ser un número decimal.
print(uniform(0, 100))

# Podemos generar un número aleatorio entre 0 y 1.
print(uniform(0, 1))

# Podemos generar un número aleatorio entre 0 y 100.
print(uniform(0, 100))

# round nos permite redondear un número decimal.
print(round(4.5))

# Podemos redondear un número decimal a un número de decimales.
print(round(4.5, 1))

# Choice nos permite elegir un elemento aleatorio de una lista.
print(choice([1, 2, 3, 4, 5]))

# Podemos elegir un elemento aleatorio de una lista de strings.
print(choice(["Hola", "Mundo", "Python"]))

# Shuffle nos permite mezclar una lista.
lista = [1, 2, 3, 4, 5]
shuffle(lista)
print(lista)

# Podemos mezclar una lista de strings.
lista = ["Hola", "Mundo", "Python"]
shuffle(lista)
print(lista)
