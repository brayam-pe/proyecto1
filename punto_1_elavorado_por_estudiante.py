# se necesita imoportar la libreria random para generar numeros aleatorios
import random

# se crea la funcion para lanzar los dados y generar dos numeros aleatorios entre 1 y 6
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# se le va a pedir el nombre al jugador 
nombre = input ("Nombre del jugador: ")

# se llama a la funcion lanzar_dados y se asignan los valores a las variables dado1 y dado2
dado1, dado2 = lanzar_dados()

# comparando los dados para determinar el resultado del juego y si son iguales o no y si el jugador puede sacar las fichas o no
if dado1 == dado2:
    print (f"Felicidades {nombre}, puedes sacar las fichas! Los dados son iguales: {dado1} y {dado2}")
else:    print (f"Lo siento {nombre},es turno del siguiente jugador, Los dados son diferentes: {dado1} y {dado2}")
