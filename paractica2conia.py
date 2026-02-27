import random

# Dice rolling game

player_name = input("Ingrese el nombre del jugador: ")
num_rolls = int(input("Ingrese el número de lanzamientos: "))

rolls = []
for i in range(num_rolls):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    rolls.append(suma)

print(f"\nJugador: {player_name}")
print(f"Lanzamientos: {rolls}")

# Categorizar lanzamientos
presadas = sum(1 for roll in rolls if roll == 6)
cinco_seis = sum(1 for roll in rolls if roll in [5, 6])
pate_perro = sum(1 for roll in rolls if roll in [1, 2])

# Calcular porcentajes
porcentaje_presadas = (presadas / num_rolls) * 100
porcentaje_cinco_seis = (cinco_seis / num_rolls) * 100
porcentaje_pate_perro = (pate_perro / num_rolls) * 100

# Imprimir resultados
print(f"\nPorcentaje 'presadas' (6): {porcentaje_presadas:.2f}%")
print(f"Porcentaje '5-6': {porcentaje_cinco_seis:.2f}%")
print(f"Porcentaje 'pate-perro' (1-2): {porcentaje_pate_perro:.2f}%")