# Adivina el numero

from random import *

print("Hola ¿Te gusta adivinar números? ¡Yo también!")
print("Para empezar dime tu nombre de jugador")
jugador = input("Nombre: ")
numero = randint(1, 101)

print(f"Bueno, {
      jugador}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")


def juego(nombre, numero):
    intentos = 0
    while True:
        intento = int(input("Intenta adivinar el número: "))
        intentos += 1
        if intentos == 8:
            print(f"¡Lo siento {nombre}! Has perdido. El número era {numero}.")
            break
        elif intento < 1 or intento > 100:
            print("El número debe estar entre 1 y 100.")
        elif intento < numero:
            print("El número que estoy pensando es mayor.")
        elif intento > numero:
            print("El número que estoy pensando es menor.")
        elif intento == numero:
            print(f"¡Felicidades {nombre}! Adivinaste el número en {
                  intentos} intentos.")
            break


juego(jugador, numero)
