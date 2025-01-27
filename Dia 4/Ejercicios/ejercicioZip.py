# Ejercicio Zip 1
# Muestra en pantalla frases como la del siguiente ejemplo:
#   La capital de Alemania es Berlín
# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

union = zip(paises, capitales)

for pais, capital in union:
    print(f"La capital de {pais} es {capital}")

# Ejercicio Zip 2

# Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.

marcas = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour"]
productos = ["Zapatos", "Playeras", "Shorts", "Calcetas", "Gorras"]

mi_zip = zip(marcas, productos)

# Ejercicio Zip 3

#   Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista
#   almacenada en la variable

espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espanol, portugues, ingles))
