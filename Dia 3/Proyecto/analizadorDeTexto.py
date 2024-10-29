# Analizador de texto

# Interfaz
print("Bienvenido al analizador de texto")
# Solicitar al usuario que introduzca un texto
texto = input("Introduce el texto que quieres analizar: ")
# Solicitar al usuario que introduzca tres letras
lista_de_letras = []
lista_de_letras.append(input("Primera letra a buscar: ").lower())
lista_de_letras.append(input("Segunda letra a buscar: ").lower())
lista_de_letras.append(input("Tercera letra a buscar: ").lower())
# Convertir el texto a minúsculas
texto_minusculas = texto.lower()
lista_de_palabras = list(texto_minusculas.split())
# Contar cuántas veces aparecen las letras en el texto
print("-"*200)
print(f"En el texto, la primera letra a buscar \"{lista_de_letras[0]}\" aparece {texto.count(lista_de_letras[0])} veces, la segunda letra a buscar \"{
      lista_de_letras[1]}\" aparece {texto.count(lista_de_letras[1])} veces y la tercera letra a buscar \"{lista_de_letras[2]}\" aparece {texto.count(lista_de_letras[2])} veces.")
# Contador de palabras en el texto
print("-"*200)
print(f"El numero de palabras en el texto es: {len(lista_de_palabras)}")
# Primera y última letra del texto
print("-"*200)
print(f"La primera lentra del texto es: \"{texto[0]}\"")
if texto[-1] == "." or texto[-1] == " ":
    print(f"La última letra del texto es: \"{texto[-2]}\"")
else:
    print(f"La última letra del texto es: \"{texto[-1]}\"")
# Invertir el texto
print("-"*200)
lista_de_palabras.reverse()
texto_al_reves = " ".join(lista_de_palabras)
texto_al_reves = texto_al_reves.capitalize()
print(texto_al_reves)
# Buscar la palabra python en el texto
print("-"*200)
bandera = "python" in lista_de_palabras
diccionario = {True: "Python aparece en el texto",
               False: "Python no aparece en el texto"}
print(diccionario[bandera])
print("-"*200)
