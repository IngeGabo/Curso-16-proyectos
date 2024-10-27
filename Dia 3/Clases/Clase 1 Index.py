# El index: En un string, el index nos permite buscar la posición de un caracter o una subcadena en un string.
# Si el caracter o la subcadena no se encuentra en el string, se genera un error.

# Ejemplo 1, index de un caracter
# En este ejemplo, buscamos la posición de la letra "a" en el string "Hola Mundo".
frase = "Hola mundo"
posicion = frase.index("a")
print(f"La letra '{frase[3]}' de la frase {
      frase} se encuentra en la posición {posicion} del string.")

# Explicaciones:
# En la línea 7, buscamos la posición de la letra "a" en el string "Hola Mundo".
# En la línea 8, imprimimos la letra que se encuentra en la posición 3 del string "Hola Mundo". Es el lugar 3 porque los strings empiezan a contar desde 0.

# Ejemplo 2, usemos numeros negativos
# En este ejemplo, imprimimos la letra que se encuentra en la posición -4 del string "Hola Mundo".
print(
    f"La letra que se encuentra en la posición -4 del string {frase} es '{frase[-4]}'.")

# Explicaciones:
# La letra que se imprime es la letra "u" porque el string "Hola Mundo" tiene 10 caracteres y el índice -4 se refiere al cuarto caracter empezando desde el final del string.

# Ejemplo 3, subcadenas de texto
# En este ejemplo, buscamos la posición de la subcadena "mundo" en el string "Hola Mundo".
posicion = frase.index("mundo")
print(f"La subcadena 'Mundo' se encuentra en la posición {
      posicion} del string.")

# Explicaciones:
# Index es sencible a mayusculas y minusculas, por lo que no encontrará la subcadena "Mundo" en el string "Hola Mundo".
# Nos regresa el index de la posición de donde inicia el substring "mundo" en el string "Hola Mundo". En este caso de la posición 5.
# En caso de no encontrar la subcadena, se generará un error.

# Ejemplo 4, index para una cadena, a partir de una posición
# En este ejemplo, pondremos a partir de una posición para buscar la letra "o" en el string "Hola Mundo".
posicion = frase.index("o", 5)
print(f"La letra '{frase[posicion]}' a partir de la posición 5 se encuentra en la posición {
      posicion} del string.")

# Explicaciones:
# Se le puede poner otra index, por ejemplo index("o", 5,7) para buscar la letra "o" entre el numero 5 y el 7.

# Ejemplo 5, usando rindex para buscar la última ocurrencia de un caracter
# El rindex es similar al index, pero busca la última ocurrencia de un caracter o subcadena en un string. Osea que empieza a buscar desde el final del string.
posicion = frase.rindex("o")
print(f"La última letra '{frase[posicion]}' se encuentra en la posición {
      posicion} del string.")

# Ejemplo 6, usando rindex para buscar la última ocurrencia de una subcadena
# En este ejemplo, buscamos la última ocurrencia de la subcadena "mundo" en el string "Hola mundo".
posicion = frase.rindex("mundo")
print(f"La última subcadena 'mundo' se encuentra en la posición {
      posicion} del string.")

# Explicaciones:
# Nos regresara la posición de la última ocurrencia de la subcadena "mundo" en el string "Hola mundo". En este caso de la posición 5, porque cuenta en la posición de la m.
