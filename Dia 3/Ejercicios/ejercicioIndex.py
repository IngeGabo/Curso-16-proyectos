# Ejercicio 1: Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"

palabra = "ordenador"
print(palabra[4])

# Ejercicio 2: Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
posicion = frase.index("práctica")
print(posicion)

# Ejercicio 3: Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
# "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

posicion = frase.rindex("práctica")
print(posicion)
