# El input es una función que nos permite pedir datos al usuario para que los ingrese por consola.

input("Pon una letra: ")

# Podemos imprimir lo que nos da el usuario
print(input("Pon tu nombre: "))

# Al poder ponerlo en un input, podemos concatenar con cadenas de texto
print("Tu nombre es: " + input("Pon tu nombre: "))

# Ahora veremos que pasa si ponemos dos input
print("Tu nombre es: " + input("Pon tu nombre: ") +
      " y tu edad es: " + input("Pon tu edad: "))
