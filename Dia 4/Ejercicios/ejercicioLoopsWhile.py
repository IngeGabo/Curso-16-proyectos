# Ejercicio Loop While 1
# Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.

i = 10
while i >= 0:
    print(i)
    i -= 1


# Ejercicio Loop While 2

# Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:
#   - Si el número es divisible por 5, mostrar dicho número en pantalla
#       (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)
#   - Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla
#       (no te olvides de seguir restando para que el programa no corra infinitamente).

i = 50
while i >= 0:
    if i % 5 == 0:
        print(i)
    i -= 1

# Ejercicio Interrupción de Flujo

# Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:

lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4,
                 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]
i = 0
while True:
    if lista_numeros[i] < 0:
        break
    print(lista_numeros[i])
    i += 1
