import random

def lanzar_dados(caras):
    return random.randint(1, caras), random.randint(1, caras)

def jugar_turno(nombre, caras):
    d1, d2 = lanzar_dados(caras)
    
    print(f"\nResultado del lanzamiento: {d1} y {d2}")
    
    es_presada = d1 == d2
    
    if es_presada:
        return f"Felicitaciones {nombre} Puedes sacar una ficha"
    else:
        return "Turno del siguiente jugador"

# Programa principal
jugador = input("Ingrese el nombre del jugador: ")

mensaje_final = jugar_turno(jugador, 6)

print(mensaje_final)