# Códigos ANSI para colores (¡Son textos normales!)
VERDE = "\033[32m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m" # 🧼 ¡CRUCIAL! Limpia la brocha para no pintar toda la pantalla
"""
Ya tenemos los colores por lo que necsitamos ahora facer todos os import que necesitemos
"""
import json

vivienda = []

try :
    with open("vivienda.json","r") as f :
        vivienda = json.load(f)
except FileNotFoundError :
    print("No se tiene un registro de la vivienda")

#Perfecto xa temos o basico posto polo que podemos empezar co codigo "unico" de este proyecto
#Ahora facemos as def de cada función do programa para asi mas adelante poder llamarla
#Funcion de registro
def registrar_habitacion() :
    nombre_habitacion = input(f"{RESET}Escriba el nombre de la habitación: ")
    try :
        numero_aparatos = int(input("Cuantos aparatos tiene la habitación?:"))
    except ValueError :
        print(f"{ROJO}Debes de introducir el nº, no letras{RESET}")
        return None
    aparatos = {}
    #Tenemos creados el nombre de la habitacion y la "cajita" de los electrodomesticos como aparatos lista
    #Ahora el bucle de electrodomesticos
    for i in range(numero_aparatos) :
            nombre_aparato = input("Nombre del aparato {}:".format(i+1))
            try :
                consumo_aparato = float(input(f"Introduce el consumo en watss del {nombre_aparato}: "))
                aparatos[nombre_aparato] = consumo_aparato
            except ValueError :
                print("Debes de introducir los watts en nº, no letra.")
                return None
            
       #Esto es el diccionario donde ya luego se guardara o cualquier cosa     
    vivienda_dict = ({
        "Habitación" : nombre_habitacion ,
        "Electrodomesticos" : aparatos
        })
    
    return vivienda_dict

    

#Función de calculo total de consumo
def calcular_total_watts(vivienda) :
    total_watts = 0
    #Asi tenemos el valor a 0 para empezar y no se contamina con otros datos
    for watts in vivienda.values() :
        total_watts += watts
    return total_watts


#Función de Categorizar o consumo en colores
def color_consumo(total_watts) :
    if total_watts < 500 :
        return f"{VERDE}{total_watts} Watts (Consumo eficiente){RESET}"
    elif total_watts <= 1500 :
        return f"{AMARILLO}{total_watts} Watts (Consumo Moderado){RESET}"
    else :
        return f"{ROJO}{total_watts} Watts (Consumo Brutal){RESET}"





while True :

    #Menu como en el anterior proyecto
    print(f"{AZUL}====================")
    print(f"Sistema Eco-Metrics ")
    print(f"====================")
    print(f"{AMARILLO}1.{RESET} Registrar Habitación y Aparatos")
    print(f"{AMARILLO}2.{RESET} Ver Reporte de Consumo Total")
    print(f"{AMARILLO}3.{RESET} Salir y Guardar")
    print(f"{AZUL}====================")
    decision = str(input(f"{RESET} Que deseas hacer?: "))
    print(f"{AZUL}====================")

    #Ahora empieza la logica de decisiones
    if decision == '1' :
        #Hacemos call a la función
        nueva_habitacion = registrar_habitacion()
        #Ahora si la funcion funciona tenemos que hacer lo siguiente
        if nueva_habitacion is not None :
            vivienda.append(nueva_habitacion)
            print(f"{VERDE}Habitación registrada con éxito{RESET}")

    elif decision == '2' :
        print(f"\n--- REPORTE ENERGETICO DE LA VIVIENDA ---")
        if len(vivienda) == 0 :
            print("No hay habitaciones registradas en el sistema.")
        
        else :
            for hab in vivienda :  #Esto hace que recorra todas las habitaciones en vivienda y las ponga 
                nom_h = hab["Habitación"]
                dict_aparatos = hab["Electrodomesticos"]

                #Pasamos a unir varias de las funciones def de antes
                total_watts = calcular_total_watts(dict_aparatos)

                #Ahora que tenemos los valores podemos ponerlos en distintos colores con la otra funcion def
                texto_pintado = color_consumo(total_watts)

                #Ahora tenemos que imprimir el informe para cada hab por eso se queda dentro del bucle for
                print(f"Habitación: {nom_h}")
                print(f"-> Total Consumo: {texto_pintado}")
                print("--------------------")
    
    else :
        
        with open("vivienda.json", "w" , encoding="utf-8") as f:
            json.dump(vivienda, f, indent=4)
        print("El reporte fue guardado en vivienda.json")
        print(f"{VERDE}Que tenga un buen dia")
        break


