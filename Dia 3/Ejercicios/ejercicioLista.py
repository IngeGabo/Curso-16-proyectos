# Ejercicio 1: Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.

mi_lista = [1, True, 23.4, "Azul", 6]


# Ejercicio 2: Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
# No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.

medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")

# Ejercicio 3: Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado.
# Utiliza métodos de listas sin alterar la línea de código ya suministrada.

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)
