# El substring es una subcadena de un string. Se puede obtener un substring de un string.
# Esto se hace con la siguiente sintaxis:

frase = "Hola mi nombre es Gabriel Garcia"
posicion_nombre = frase.index("Gabriel")
posicion_apellido = frase.rindex("a")
# Es necesario sumar 1 porque la fragmentación de strings no incluye el indice que pusiste al final.
substring = frase[posicion_nombre:posicion_apellido+1]
print(substring)

# Ahora vamos a hacer un ejemplo para ver las otras formas de hacerlo
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
subcadena = letras[0:5]
print(subcadena)  # "ABCDE"
subcadena = letras[5:]
print(subcadena)  # "FGHIJKLMNOPQRSTUVWXYZ"
subcadena = letras[:5]
print(subcadena)  # "ABCDE"
subcadena = letras[5:10]
print(subcadena)  # "FGHIJ"
# El 2 del final es el paso, es decir, que se salte de 2 en 2.
subcadena = letras[5:10:2]
print(subcadena)  # "FHJ"
# Si el paso es positivo, va a ir de izquierda a derecha.
subcadena = letras[::2]
print(subcadena)  # "ACEGIKMOQSUWY"
# Si el paso es negativo, se va a ir de derecha a izquierda.
subcadena = letras[10:5:-1]
print(subcadena)  # "KJIHG"
subcadena = letras[::-1]  # Si no pones nada, va a ir de izquierda a derecha.
print(subcadena)  # "ZYXWVUTSRQPONMLKJIHGFEDCBA"
# Si el paso es negativo, va a ir de derecha a izquierda.
subcadena = letras[::-2]
print(subcadena)  # "ZWTQNMLKHFDB"
# Si el paso es positivo, se va a ir de izquierda a derecha.
subcadena = letras[10:5:1]
# "" En este caso va a ser vacío porque el paso es positivo y el inicio es mayor que el final.
print(subcadena)

# Un slicing tiene la siguiente forma: [inicio:final:paso]
