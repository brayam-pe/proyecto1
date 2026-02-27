import random

# Dice rolling game

player_name = input("Ingrese el nombre del jugador: ")
num_rolls = int(input("Ingrese el número de lanzamientos: "))

rolls = []
for i in range(num_rolls):
    roll = random.randint(1, 6)
    rolls.append(roll)

print(f"\nJugador: {player_name}")
print(f"Lanzamientos: {rolls}")
def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

dado1, dado2 = lanzar_dados()
print(f"Suma total de dados: {dado1 + dado2}")

if dado1 == dado2:
    print(f"Felicidades {player_name}, puedes sacar las fichas! Los dados son iguales: {dado1} y {dado2}")
else:
    print(f"Lo siento {player_name}, es turno del siguiente jugador. Los dados son diferentes: {dado1} y {dado2}")