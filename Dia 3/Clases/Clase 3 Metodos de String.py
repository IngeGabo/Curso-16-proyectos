# Metodos del String

# Metodo 1: Upper()
# Este método se usa para convertir todas las letras del string en mayúsculas.

string_ejemplo = "Hola Mundo"
print(string_ejemplo.upper())  # "HOLA MUNDO"

# Metodo 2: Lower()
# Este método se usa para convertir todas las letras del string en minúsculas.

print(string_ejemplo.lower())  # "hola mundo"

# Metodo 3: Capitalize()
# Este método se usa para convertir todas las letras del string en minúsculas, excepto la primera letra, que se convierte en mayúscula.

print(string_ejemplo.capitalize())  # "Hola mundo"

# Metodo 4: Title()
# Este método se usa para convertir la primera letra de cada palabra en mayúscula.

# Los voy a convertir a minúsculas para que se vea mejor.
string_ejemplo = string_ejemplo.lower()
print(string_ejemplo.title())  # "Hola Mundo"

# Metodo 5: Swapcase()
# Este método se usa para convertir las mayúsculas en minúsculas y viceversa.

string_ejemplo = "Hola Mundo"  # Regresemos al estado base.
print(string_ejemplo.swapcase())  # "hOLA mUNDO"

# Metodo 6: Isupper()
# Este método se usa para verificar si todas las letras del string están en mayúsculas.

print(string_ejemplo.isupper())  # False
string_ejemplo = string_ejemplo.upper()
print(string_ejemplo.isupper())  # True

# Metodo 7: Islower()
# Este método se usa para verificar si todas las letras del string están en minúsculas.

print(string_ejemplo.islower())  # False
string_ejemplo = string_ejemplo.lower()
print(string_ejemplo.islower())  # True

# Metodo 8: Isalpha()
# Este método se usa para verificar si el string contiene solo letras.

string_ejemplo = "HolaMundo"
print(string_ejemplo.isalpha())  # True
string_ejemplo = "Hola Mundo"
print(string_ejemplo.isalpha())  # False

# Metodo 9: Isalnum()
# Este método se usa para verificar si el string contiene solo letras y números.

string_ejemplo = "HolaMundo123"
print(string_ejemplo.isalnum())  # True
string_ejemplo = "Hola Mundo"
print(string_ejemplo.isalnum())  # False

# Metodo 10: Isdigit()
# Este método se usa para verificar si el string contiene solo números.

string_ejemplo = "123"
print(string_ejemplo.isdigit())  # True
string_ejemplo = "Hola Mundo"
print(string_ejemplo.isdigit())  # False

# Metodo 11: Isdecimal()
# Este método se usa para verificar si el string contiene solo números decimales.

string_ejemplo = "123.456"
print(string_ejemplo.isdecimal())  # True
string_ejemplo = "Hola Mundo"
print(string_ejemplo.isdecimal())  # False

# Metodo 12: Isnumeric()
# Este método se usa para verificar si el string contiene solo números.

string_ejemplo = "½3"
print(string_ejemplo.isnumeric())  # True
string_ejemplo = "Hola Mundo"
print(string_ejemplo.isnumeric())  # False

# Diferencia entre Isnumeric() y Isdigit() es la siguiente: Isnumeric() puede contener números que no son dígitos, como números romanos, números fraccionarios, subíndices y superíndices.

# Metodo 13: Isspace()
# Este método se usa para verificar si el string contiene solo espacios.

string_ejemplo = " "
print(string_ejemplo.isspace())  # True
string_ejemplo = "Hola Mundo"
print(string_ejemplo.isspace())  # False

# Metodo 14: Startswith()
# Este método se usa para verificar si el string comienza con el valor especificado.

print(string_ejemplo.startswith("Hola"))  # True
print(string_ejemplo.startswith("Mundo"))  # False

# Metodo 15: Endswith()
# Este método se usa para verificar si el string termina con el valor especificado.

print(string_ejemplo.endswith("Mundo"))  # True
print(string_ejemplo.endswith("Hola"))  # False

# Metodo 16: Find()
# Este método se usa para buscar la primera aparición del valor especificado.

print(string_ejemplo.find("Mundo"))  # 5
print(string_ejemplo.find("Hola"))  # 0
print(string_ejemplo.find("Perro"))  # -1

# La principal diferencia entre find() y index() es que index() arroja un error si no encuentra el valor especificado, mientras que find() arroja -1.

# Metodo 17: Index()
# Este método se usa para buscar la primera aparición del valor especificado.

print(string_ejemplo.index("Mundo"))  # 5
print(string_ejemplo.index("Hola"))  # 0
# print(string_ejemplo.index("Perro"))  # ValueError: substring not found

# Metodo 18: Rfind()
# Este método se usa para buscar la última aparición del valor especificado.

string_ejemplo = "Hola Mundo Hola"
print(string_ejemplo.rfind("Hola"))  # 11

# Metodo 19: Rindex()
# Este método se usa para buscar la última aparición del valor especificado.

print(string_ejemplo.rindex("Hola"))  # 11
string_ejemplo = "Hola Mundo"  # Lo regresamos a su estado base.

# Metodo 20: Count()
# Este método se usa para contar cuántas veces aparece el valor especificado.

print(string_ejemplo.count("o"))  # 2
print(string_ejemplo.count("Hola"))  # 1

# Metodo 21: Replace()
# Este método se usa para reemplazar una cadena con otra cadena.

print(string_ejemplo.replace("Hola", "Adiós"))  # "Adiós Mundo"
print(string_ejemplo.replace("Mundo", "Mundos"))  # "Hola Mundos
print(string_ejemplo.replace("Mundos", "Perro"))  # "Hola Mundo"

# Metodo 22: Split()
# Este método se usa para dividir el string en una lista.

print(string_ejemplo.split())  # ["Hola", "Mundo"]

# Metodo 23: Join()
# Este método se usa para unir los elementos de una lista en un string.

lista = ["Hola", "Mundo"]
print(" ".join(lista))  # "Hola Mundo"

# Metodo 24: Strip()
# Este método se usa para eliminar los espacios en blanco al principio y al final del string.

string_ejemplo = " Hola Mundo "
print(string_ejemplo.strip())  # "Hola Mundo"

# Metodo 25: Lstrip()
# Este método se usa para eliminar los espacios en blanco al principio del string.

print(string_ejemplo.lstrip())  # "Hola Mundo "

# Metodo 26: Rstrip()
# Este método se usa para eliminar los espacios en blanco al final del string.

print(string_ejemplo.rstrip())  # " Hola Mundo"

# Metodo 27: Center()
# Este método se usa para centrar el string.

string_ejemplo = "Hola Mundo"  # Regresamos al estado base.
# "-----Hola Mundo-----" Ahora son 20 caracteres contando la base y los guiones.
print(string_ejemplo.center(20, "-"))

# Metodo 28: Ljust()
# Este método se usa para justificar el string a la izquierda.

print(string_ejemplo.ljust(20, "-"))  # "Hola Mundo----------"

# Metodo 29: Rjust()
# Este método se usa para justificar el string a la derecha.

print(string_ejemplo.rjust(20, "-"))  # "----------Hola Mundo"

# Metodo 30: Zfill()
# Este método se usa para rellenar el string con ceros.

string_ejemplo = "42"
print(string_ejemplo.zfill(5))  # Salida: "00042"

string_ejemplo = "-42"
print(string_ejemplo.zfill(5))  # Salida: "-0042"


# Metodo 31: Partition()
# Este método divide el string en una tupla.

string_ejemplo = "Hola Mundo"
print(string_ejemplo.partition(" "))  # ("Hola", " ", "Mundo")

# Metodo 32: Rpartition()
# Este método divide el string en una tupla.

string_rpartition = "Hola Mundo Rpartition"
print(string_rpartition.rpartition(" "))  # ("Hola", " ", "Mundo Rpartition")

# Metodo 33: Maketrans()
# Este método se usa para crear una tabla de traducción.

string_ejemplo = "Hola Mundo"
tabla = string_ejemplo.maketrans("aeiou", "12345")
print(tabla)  # {97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
string_ciflado = string_ejemplo.translate(tabla)
print(string_ciflado)  # "H4l1 M5nd4"

# Por ultimo recuerda que tambien puedes hacer estos metodos para solo una parte del string, por ejemplo:

string_ejemplo = "Hola Mundo"
print(string_ejemplo[:4].upper())  # "HOLA"
