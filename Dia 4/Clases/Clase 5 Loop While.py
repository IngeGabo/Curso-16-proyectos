# Loop while: El loop while se ejecuta mientras la condición sea verdadera. Sirve la condición para que el loop se ejecute, se ejecuta el bloque de código y
# se vuelve a evaluar la condición. Si la condición es verdadera, se ejecuta el bloque de código y se vuelve a evaluar la condición. Si la condición es falsa,
# se sale del loop.

# Ejemplo 1: Loop while
i = 0
while i < 5:
    print(i)
    i += 1
print("El loop ha finalizado")

# Ejemplo 2: Loop while
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("El loop ha finalizado")

# Ejemplo 3: Loop while break
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break  # Se sale del loop
else:
    print("El loop ha finalizado")

# Ejemplo 4: Loop while continue
i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("El loop ha finalizado")

# Ejemplo 5: Loop while pass
i = 0
while i < 5:
    if i == 3:
        pass
    print(i)
    i += 1
else:
    print("El loop ha finalizado")

# Ejemplo 6: Simulación de Loop do while
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

# Ejemplo 7: Loop while con input
while True:
    x = input("Ingrese un número: ")
    if x == "salir":
        break
    print(x)

# Ejemplo 8: Loop while con una lista
lista = [4, 5, 6, 7, 8]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1
