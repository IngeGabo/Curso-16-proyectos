# El redondeo es una operación matemática que se utiliza para aproximar un número a otro número más cercano.
# Se redondeo se utiliza cuando una operación matemática da como resultado un número con decimales, y se desea que el resultado sea un número entero.

# Para redondear un número en Python, se utiliza la función round().
# La función round() toma un número como argumento, y devuelve el número redondeado al entero más cercano.

# Ejemplo:
# Tenemos una operación con muchos decimales
import math  # Importamos el módulo math para utilizar las funciones ceil() y floor()
operacion = 90 / 7
print(operacion)  # 12.857142857142858
# Redondeamos el resultado de la operación
print(round(operacion))  # 13
# Si queremos que deje un numero de decimales especifico, podemos pasar un segundo argumento a la función round()
print(round(operacion, 2))  # 12.86

# El redondear un número en Python, toma en consideración que si el ultimo digito es =< 5, se redondea hacia abajo, si es > 5, se redondea hacia arriba.
# Si el ultimo digito es 5, se redondea hacia arriba si el digito anterior es impar, y hacia abajo si es par.
# Ejemplo:
print(round(2.4))  # 2
print(round(2.6))  # 3
print(round(2.5))  # 2
print(round(3.5))  # 4

# Si queremos redondear un número hacia arriba, podemos utilizar la función ceil() del módulo math.
# ejemplos:
print(math.ceil(2.3))  # 3
# Si queremos redondear un número hacia abajo, podemos utilizar la función floor() del módulo math.
# ejemplos:
print(math.floor(2.7))  # 2
