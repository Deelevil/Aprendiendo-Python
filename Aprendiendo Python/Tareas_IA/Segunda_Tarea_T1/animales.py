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
    decision = input("Desea introducir un nuevo animal? (s/n):")
    if decision.lower() == 'n':
        break
    try:
        n = int(input("Cuantos animales quires introducir?:"))
        info_refugio = {}
        
            #Tenemos a variable de repetición e o diccionario de cada animal
        for i in range(n):
            try:
                nombre = input("Nº del Chip {}:".format(i+1))
                especie = input("Nombre de la especie {} :".format(i+1))
                caracteristicas_n = int(input("Total de caracteristicas del animal {}".format(i+1)))
                caracteristicas_b = {}
                for j in range(caracteristicas_n):
                    concepto = input("Que tipo de caracteristica es?(ej:Planeta,Peligroso,etc):")
                    cualidad = input(f"Ingrese la caracteristica ")
                    #Ahora guardamos esta mini cajita jejejeje
                    caracteristicas_b[concepto] =  cualidad

                refugio.append({
                "Chip id" : nombre,
                "Especie" : especie,
                "caracteristicas" : caracteristicas_b
                }) 
            except ValueError :
                print("Ocurrio un error de nº. Revisa bien los formatos que introduzcas")



   
    except Exception as error:
        print("Ocurrio un error inesperado", str(error))

exportar = input("Desea exportar los datos a un formato JSON?  (s/n):")
if exportar.lower() == 's' :
        with open("refugio.json" , "w") as f:
            json.dump (refugio , f , indent=4)
            print("Datos exportados correctamente")
else:
    print("Exportación cancelada")
    


#Linea Final