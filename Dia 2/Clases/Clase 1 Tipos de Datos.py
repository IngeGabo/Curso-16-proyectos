# Clase 1
# Tipos de Datos
# Simples
# Interger: Numeros enteros, pueden ser positivos o negativos
numero = 10
numeroNegativos = -10
# Float: Numeros decimales, pueden ser positivos o negativos
numeroDecimal = 10.5
numeroDecimalNegativo = -10.5
# Boolean: Numeros booleanos, pueden ser True o False
verdadero = True
falso = False
# Char: Caracteres, pueden ser letras, numeros o simbolos, se declaran con comillas simples o dobles
letra = 'a'
numero = "1"
simbolo = "!"

# Complejos
# String: Cadena de caracteres, se declaran con comillas simples o dobles
# Uso: Se usan Strings para almacenar texto
cadena = "Hola Mundo"
# List: Lista de elementos, se declaran con corchetes
# Uso: Se usan Listas para almacenar varios elementos, pueden ser de diferentes tipos
lista = [1, 2, 3, 4, 5]
listaMixta = [1, 2, 3, "Hola", True]
# Tuple: Tupla de elementos, se declaran con parentesis
# Uso: Se usan Tuplas para almacenar varios elementos, pueden ser de diferentes tipos
tupla = (1, 2, 3, 4, 5)
tuplaMixta = (1, 2, 3, "Hola", True)
# Set: Conjunto de elementos, se declaran con llaves
# Uso: Se usan Sets para almacenar varios elementos, no pueden ser de diferentes tipos
conjunto = {1, 2, 3, 4, 5}
conjuntoMixto = {1, 2, 3, "Hola", True}
# Dictionary: Diccionario de elementos, se declaran con llaves
# Uso: Se usan Diccionarios para almacenar varios elementos, se almacenan como clave-valor
diccionario = {"nombre": "Juan", "apellido": "Perez", "edad": 25}

# Diferencia entre lista, tupla, set y diccionario:
# Lista: Se declaran con corchetes, se pueden modificar
# Tupla: Se declaran con parentesis, no se pueden modificar
# Set: Se declaran con llaves, no se pueden modificar y no pueden tener elementos repetidos
# Diccionario: Se declaran con llaves, se almacenan como clave-valor
print(
    f"numero: {numero}\n"
    f"numeroNegativos: {numeroNegativos}\n"
    f"numeroDecimal: {numeroDecimal}\n"
    f"numeroDecimalNegativo: {numeroDecimalNegativo}\n"
    f"verdadero: {verdadero}\n"
    f"falso: {falso}\n"
    f"letra: {letra}\n"
    f"numero: {numero}\n"
    f"simbolo: {simbolo}\n"
    f"cadena: {cadena}\n"
    f"lista: {lista}\n"
    f"listaMixta: {listaMixta}\n"
    f"tupla: {tupla}\n"
    f"tuplaMixta: {tuplaMixta}\n"
    f"conjunto: {conjunto}\n"
    f"conjuntoMixto: {conjuntoMixto}\n"
    f"diccionario: {diccionario}"
)
