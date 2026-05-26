#Nueva actividade dada pola IA. Parecido ao anterior, pero esta vez con mascotas. Lets gooooo
import json
#Paso importante, facer donde estan as listas
refugio = []

try:
    with open("refugio.json","r") as f:
        refugio = json.load(f)
except FileNotFoundError :
    print("No se encontro datos guardados. Se crearan al terminar")

while True :
    decision = input("Desea introducir un nuevo animal? (s/n)")
    if decision.lower() == 'n':
        break
    try:
        n = input("Cuantos animales quires introducir?")
        info_refugio = {}
        #Tenemos a variable de repetición e o diccionario de cada animal
        for i in range(n):
            nombre = input("Nº del Chip {}".format(i+1))
            especie = input("Nombre de la especie {}".format(i+1))
            caracteristicas_n = input("Total de caracteristicas del animal {}".format(i+1))
    



    except ValueError:
        print("Fijate en los formatos de datos que estas añadiendo")
    except Exception as error:
        print("Ocurrio un error inesperado", str(error))

#Linea Final


