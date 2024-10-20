# Los operadores son símbolos que permiten realizar operaciones sobre los datos.
# Los operadores se dividen en:
# - Operadores aritméticos
# - Operadores de comparación
# - Operadores lógicos
# - Operadores de asignación
# - Operadores de identidad
# - Operadores de membresía
# - Operadores de bits

# Digitos con los que vamos a estar trabajando
a = 10
b = 8

# Operadores aritméticos
# Los operadores aritméticos se utilizan para realizar operaciones matemáticas.
# + Suma
print(f"La suma de {a} + {b} es: {a + b}")
# - Resta
print(f"La resta de {a} - {b} es: {a - b}")
# * Multiplicación
print(f"La multiplicación de {a} * {b} es: {a * b}")
# / División
print(f"La división de {a} / {b} es: {a / b}")
# // División entera
# Devuelve el cociente de la división
print(f"La división entera de {a} // {b} es: {a // b}")
# % Módulo
# Devuelve el residuo de la división
print(f"El módulo de {a} % {b} es: {a % b}")
# ** Exponente
print(f"El exponente de {a} ** {b} es: {a ** b}")
# **0.5 raíz cuadrada
print(f"La raíz cuadrada de {a} es: {a ** 0.5}")

# Operadores de comparación
# Los operadores de comparación se utilizan para comparar dos valores.
# == Igual
print(f"¿{a} es igual a {b}?: {a == b}")
# != Diferente
print(f"¿{a} es diferente a {b}?: {a != b}")
# > Mayor que
print(f"¿{a} es mayor que {b}?: {a > b}")
# < Menor que
print(f"¿{a} es menor que {b}?: {a < b}")
# >= Mayor o igual que
print(f"¿{a} es mayor o igual que {b}?: {a >= b}")
# <= Menor o igual que
print(f"¿{a} es menor o igual que {b}?: {a <= b}")

# Operadores lógicos
# Los operadores lógicos se utilizan para combinar declaraciones condicionales.
# and Devuelve True si ambas declaraciones son verdaderas
print(f"¿{a} es mayor que 5 y {b} es menor que 10?: {a > 5 and b < 10}")
# or Devuelve True si al menos una de las declaraciones es verdadera
print(f"¿{a} es mayor que 5 o {b} es menor que 10?: {a > 5 or b < 10}")
# not Invierte el resultado, devuelve False si el resultado es verdadero
print(f"¿No es cierto que {a} es mayor que 5?: {not a > 5}")

# Operadores de asignación
# Los operadores de asignación se utilizan para asignar valores a las variables.
# = Asignación
c = a
print(f"El valor de c es: {c}")
# += Suma y asignación
c += a  # c = c + a
print(f"El valor de c es: {c}")
# -= Resta y asignación
c -= a  # c = c - a
print(f"El valor de c es: {c}")
# *= Multiplicación y asignación
c *= a  # c = c * a
print(f"El valor de c es: {c}")
# /= División y asignación
c /= a  # c = c / a
print(f"El valor de c es: {c}")
# //= División entera y asignación
c //= a  # c = c // a
print(f"El valor de c es: {c}")
# %= Módulo y asignación
c %= a  # c = c % a
print(f"El valor de c es: {c}")
# **= Exponente y asignación
c **= a  # c = c ** a
print(f"El valor de c es: {c}")

# Operadores de identidad
# Los operadores de identidad se utilizan para comparar objetos, no si son iguales, sino si son el mismo objeto.
# is Devuelve True si ambas variables son el mismo objeto
print(f"¿a y b son el mismo objeto?: {a is b}")
# is not Devuelve True si ambas variables no son el mismo objeto
print(f"¿a y b no son el mismo objeto?: {a is not b}")

# Operadores de membresía
# Los operadores de membresía se utilizan para probar si una secuencia se encuentra en un objeto.
# in Devuelve True si un valor específico está presente en el objeto
lista = [1, 2, 3, 4, 5]
print(f"¿El número 3 está en la lista?: {3 in lista}")
# not in Devuelve True si un valor específico no está presente en el objeto
print(f"¿El número 6 no está en la lista?: {6 not in lista}")

# Operadores de bits
# Los operadores de bits se utilizan para comparar números (en forma binaria).
# & AND
print(f"El resultado de 10 & 8 es: {10 & 8}")
# | OR
print(f"El resultado de 10 | 8 es: {10 | 8}")
# ^ XOR
print(f"El resultado de 10 ^ 8 es: {10 ^ 8}")
# ~ NOT
print(f"El resultado de ~10 es: {~10}")
# << Desplazamiento a la izquierda
print(f"El resultado de 10 << 1 es: {10 << 1}")
# >> Desplazamiento a la derecha
print(f"El resultado de 10 >> 1 es: {10 >> 1}")

# Operadores de precedencia
# Los operadores de precedencia se utilizan para determinar el orden de ejecución de los operadores.
# Los operadores con mayor precedencia se ejecutan primero.
# Los operadores de precedencia son:
# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. <, <=, >, >=
# 6. ==, !=
# 7. not
# 8. and
# 9. or
print(f"El resultado de 10 + 8 * 2 es: {10 + 8 * 2}")
