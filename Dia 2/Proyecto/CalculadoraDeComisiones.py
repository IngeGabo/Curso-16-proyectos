# Esto es una calculadora de comisiones, en base a un monto de venta, donde se solicita el nombre y el monto de venta, redondeado a dos decimales
# Versión estudiante

nombre = input("¿Cuál es tu nombre? ")
ventas = int(input("¿Cuanto vendiste en el mes? "))
comision = round(ventas * 13 / 100, 2)  # Tambien podria ser ventas * 0.13
print(f"Hola {nombre}, tu comisión es de ${comision} ¡Felicitaciones!")
