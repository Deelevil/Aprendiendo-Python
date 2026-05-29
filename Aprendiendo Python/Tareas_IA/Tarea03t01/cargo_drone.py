#Ahora importamos e abrimos a lista vacia


# Códigos ANSI para colores (¡Son textos normales!)
VERDE = "\033[32m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m" # 🧼 ¡CRUCIAL! Limpia la brocha para no pintar toda la pantalla

import json
flota = []

try :
    with open("flota.json","r") as f :
        flota = json.load(f)
except FileNotFoundError :
    print("No se tiene un registro de flota")

#Ahora que temos leido se temos documentos podemos abrir o programa

while True :
    print("===================================")
    print("      ---Sistema Cargo-Sky---      ")
    print("===================================")

    print(f"{AMARILLO}1.{RESET} Registrar un nuevo Dron ")
    print(f"{AMARILLO}2.{RESET} Ver estado de la Flota")
    print(f"{AMARILLO}3.{RESET} Salir")

    print("===================================")
   
   
   #Ahora temos que cada vez que se repite o bucle volve a salir o IU
   
   
    x = str(input("Que quieres hacer?:"))
    
    #Tambien se repite a pregunta de que se quere facer co input

    if x.lower() == '1' :
        print("Ingrese los datos por favor: ")
        id_Dron = input("Ingrese el id del Dron: ")
        md = input("Ingrese el modelo del Dron: ")
        try :
            bateria = float(input("Ingrese el porcentaje de la Bateria: "))
        except ValueError :
            print("Debe de poner un nº entero:")
            continue

        #Ahora tenemos el guardado de la lista
        print("Datos guardados")

        flota.append({
            "Id del Dron" : id_Dron ,
            "Modelo del Dron" : md ,
            "Bateria del Dron" : bateria
        })
    
    #Ahora tenemos la segunda
    
    if x.lower() == '2' : 
        print("Estado de la Flota")
        try:
            for id_Dron in flota :
                idd = id_Dron ["Id del Dron"]
                mdd = id_Dron ["Modelo del Dron"]
                bt = id_Dron ["Bateria del Dron"]
                print(f"Id del Dron: {idd}")
                print(f"Modelo del Dron: {mdd}")
                if bt <= 25 :
                    print(f"|-- ALERTA --| Bateria del Dron: {bt} esta baja ")
                else :
                    print(f"Bateria del Dron: {bt}")

                print("==========================")
        
        
        except NameError :
            print("No se pudo cargar la Flota")


    #Ahora facemos a terceira opción do menu

    if x.lower() == '3' :
        exportar = input("Desea Guardar los cambios?: (s/n) :")
        if exportar.lower() == 'n':
            print("Que tenga un buen dia")
            break 
        if exportar == 's' :
            with open("flota.json", "w") as f:
                json.dump(flota, f, indent=4)
                print("Datos exportados a flota.json")
                break
            
             
        
    

    