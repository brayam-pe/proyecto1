import random

# Juego de lanzar dos dados

nombre_jugador = input("Escriba el nombre del jugador: ")
cantidad_lanzamientos = int(input("¿Cuántos lanzamientos quiere hacer?: "))

lista_lanzamientos = []

# Hacemos los lanzamientos
for i in range(cantidad_lanzamientos):
    dado_uno = random.randint(1, 6)
    dado_dos = random.randint(1, 6)
    suma_dados = dado_uno + dado_dos
    
    lista_lanzamientos.append(suma_dados)

print("\nJugador:", nombre_jugador)
print("Resultados de los lanzamientos:", lista_lanzamientos)

# Contadores
contador_presadas = 0
contador_cinco_seis = 0
contador_pate_perro = 0

# Revisamos cada lanzamiento
for resultado in lista_lanzamientos:
    
    if resultado == 6:
        contador_presadas += 1
    
    if resultado == 5 or resultado == 6:
        contador_cinco_seis += 1
    
    if resultado == 1 or resultado == 2:
        contador_pate_perro += 1

# Calculamos los porcentajes
porcentaje_presadas = (contador_presadas / cantidad_lanzamientos) * 100
porcentaje_cinco_seis = (contador_cinco_seis / cantidad_lanzamientos) * 100
porcentaje_pate_perro = (contador_pate_perro / cantidad_lanzamientos) * 100

# Mostramos resultados
print("\nPorcentaje de presadas (cuando sale 6):", round(porcentaje_presadas, 2), "%")
print("Porcentaje cuando sale 5 o 6:", round(porcentaje_cinco_seis, 2), "%")
print("Porcentaje de pate-perro (cuando sale 1 o 2):", round(porcentaje_pate_perro, 2), "%")
