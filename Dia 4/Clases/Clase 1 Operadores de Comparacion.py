# Un Operador de Comparación es un símbolo que se utiliza para comparar dos valores. Los operadores de comparación son:
# == comparación de igualdad
# != comparación de desigualdad
# > comparación de mayor que
# < comparación de menor que
# >= comparación de mayor o igual que
# <= comparación de menor o igual que

# Ejemplo de uso de operadores de comparación:
# Comparación de igualdad
print(5 == 5)  # True
print(5 == 6)  # False
# Comparación de desigualdad
print(5 != 5)  # False
print(5 != 6)  # True
# Comparación de mayor que
print(5 > 5)  # False
print(5 > 6)  # False
print(6 > 5)  # True
# Comparación de menor que
print(5 < 5)  # False
print(5 < 6)  # True
print(6 < 5)  # False
# Comparación de mayor o igual que
print(5 >= 5)  # True
print(5 >= 6)  # False
print(6 >= 5)  # True
# Comparación de menor o igual que
print(5 <= 5)  # True
print(5 <= 6)  # True
print(6 <= 5)  # False

# Asignarlo a una variable
a = 5 == 5
print(a)  # True

# Comparación de igualdad de tipos de datos diferentes
print(5 == "5")  # False
print(5 == 5.0)  # True
