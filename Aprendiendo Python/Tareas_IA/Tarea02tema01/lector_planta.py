#Sacar un json con información e facer un display bonito
import os
print("Python está buscando tus archivos en la carpeta:", os.getcwd())
import json 
print("=====================================")
print("         SISTEMA DE CONTROL          ")
print("=====================================")

try:
    with open("planta.json","r") as f :
        planta = json.load(f)
except FileNotFoundError :
    print("No existen datos de la planta")

#Non me lee os datos e non sei por que.

try :
    for id_reactor in planta :
        re = id_reactor ["id_reactor"]
        ub = id_reactor ["ubicacion"]
        te = id_reactor ["telemetria"] ["temperatura_c"]
        pr = id_reactor ["telemetria"] ["presion_bar"]
        es = id_reactor ["telemetria"] ["estado"]
    
        print(f"Reactor: {re} | Ubicación: {ub} ")
        print(f"-> Temperatura: {te} ºC")
        print(f"-> Presión: {pr}")
        if es == "Critico" :
            print(f"[⚠️ ALERTA MÁXIMA] REACTOR {re} EN ESTADO CRÍTICO")
        else :
            print(f"Estado del Reactor: {es}")
        
        print("==============================")
 #Ahora xa nos aparece todo bonito

except NameError :
    print("No se puede mostrar el tablero, no se cargaron los datos")
except Exception as error :
    print("Ocurrio el error:", str(error))


print("=====================================")