import random

def lanzar_hasta_obtener(valor_buscado):
    
    contador_lanzamientos = 0
    suma_dados = 0
    
    # Validamos que el número esté entre 2 y 12
    if valor_buscado < 2 or valor_buscado > 12:
        print("El número debe estar entre 2 y 12.")
        return None
    
    # Repetimos hasta que salga el número buscado
    while suma_dados != valor_buscado:
        
        dado_uno = random.randint(1, 6)
        dado_dos = random.randint(1, 6)
        suma_dados = dado_uno + dado_dos
        
        contador_lanzamientos += 1
        
        print("Lanzamiento", contador_lanzamientos, 
              "-> Dado 1:", dado_uno, 
              "Dado 2:", dado_dos, 
              "Suma:", suma_dados)
    
    return contador_lanzamientos


# Programa principal
numero_deseado = int(input("Ingrese un número entre 2 y 12: "))

cantidad = lanzar_hasta_obtener(numero_deseado)

if cantidad != None:
    print("\nSe necesitó", cantidad, "lanzamientos para obtener el número", numero_deseado)
