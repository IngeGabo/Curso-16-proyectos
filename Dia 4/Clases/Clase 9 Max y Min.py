# Maximos y minimos: Los maximos y minimos de una lista se pueden obtener con las funciones max() y min() respectivamente.

import random

# ## Ejercicio 1: Obtener el máximo y mínimo de una lista

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# mezclar la listaNumeros

random.shuffle(listaNumeros)
print(listaNumeros)

maximo = max(listaNumeros)
minimo = min(listaNumeros)

print(f"El máximo de la lista es {maximo}")
print(f"El mínimo de la lista es {minimo}")

# ## Ejercicio 2: Obtener el máximo y mínimo de una lista de strings

listaNombres = ["Juan", "Pedro", "Ana", "María",
                "José", "Luis", "Carlos", "Sofía", "Marta", "Lucía"]
# mezclar la listaNombres

random.shuffle(listaNombres)
print(listaNombres)

# En el máximo de la lista de strings se considera el orden alfabético enntonces el resultado es el último elemento de la lista
maximo = max(listaNombres)
# En el mínimo de la lista de strings se considera el orden alfabético enntonces el resultado es el primer elemento de la lista
minimo = min(listaNombres)

print(f"El máximo de la lista es {maximo}")  # Sofía
print(f"El mínimo de la lista es {minimo}")  # Ana

# ## Ejercicio 3: Obtener el máximo y mínimo de una lista de tuplas

listaTuplas = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# mezclar la listaTuplas

random.shuffle(listaTuplas)
print(listaTuplas)


# En el máximo de la lista de tuplas se considera el primer elemento de la tupla
maximo = max(listaTuplas)
# En el mínimo de la lista de tuplas se considera el primer elemento de la tupla
minimo = min(listaTuplas)

print(f"El máximo de la lista es {maximo}")  # (9, 10)
print(f"El mínimo de la lista es {minimo}")  # (1, 2)
