# Códigos ANSI para colores (¡Son textos normales!)
VERDE = "\033[32m"
ROJO = "\033[31m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m" # 🧼 ¡CRUCIAL! Limpia la brocha para no pintar toda la pantalla
"""
Ya tenemos los colores por lo que necsitamos ahora facer todos os import que necesitemos
"""
caja_fuerte = []

import json
import random

try :
    with open("caja_fuerte.json","r") as f :
        caja_fuerte = json.load(f)
except FileNotFoundError :
    print("El vault esta vacio")

#Esta función o que fai e analizar se a contraseña ten o nº de caracteres requeridos (futura melloria seria analizar tamen: Mayusculas,numeros,simbolos)
def validador_contraseña(password) :

    if len(password) >= 8  :
        return True
    else :
        return False
    
#Creo que esta función o que fai e ocultar o principio da contraseña, ocultando a primeira mitad
def ocultar_llave(password) :
    #No entiendo que quiere hacer el [:2]/[-2:]
    return f"{password[:2]}****{password[-2:]}"

#Función para poner de color o nivel de seguridad que presenta a contraseña
def calcular_seguridad(password) :
    #Texto que se use en funciones con def SEMPRE SE USA sin colores. Xa se modifican despois.
    if len(password) <=11 :
        return f"MEDIA"
    else :
        return f"ALTA"
    
#Función que crea as contraseñas de forma aleatoria
def generador_contrasenas_aleatorio() :
    #Ahora faise a lista con todos os posibles caracteres que pode coller o generador
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*#$"
    nueva_clave =""

    #Ahora hacemos el bucle para generar contraseñas con random
    for i in range(12) :
        nueva_clave += random.choice(caracteres)
    
    return nueva_clave

#Función mas larga dado a que seria unha parte enteira do menu principal sendo solo modular jajajaajaja
def crear_credenciales() :
    nombre_plataforma = str(input(f"{AZUL}De que es la contraseña?{RESET} "))
    nombre_usuario = str(input(f"{AZUL}Cual es el usuario?{RESET} "))
    accion = input(f"{AZUL}¿Desea {AMARILLO}(1){AZUL}Escribir tu contraseña o {AMARILLO}(2){AZUL}Generar una aleatoria segura?{RESET} ")
    #Elegimos crear contraseña propia
    if accion == '1' :
       while True :
           password = str(input(f"Introduzca la contreña que desea: "))
            #Non funcionaba antes, ahora si, antes a o non ter a función en un if, volviase un bucle infinito
           if validador_contraseña(password) :
               print(f"{VERDE}La contraseña es buena.{RESET} ")
               break
           else :
               print(f"{ROJO}Contraseña demasiado corta, vuelvalo a intentar.{RESET} ")
           
           

    else :    
       
       password = generador_contrasenas_aleatorio()
       print(f"Tu contrasela generada es:{AMARILLO}{password}{RESET}")
       

    nivel_seguridad = calcular_seguridad(password)
    #Calcula a seguridade da contraseña, dando igual se foi aleatoria ou creada pro ti
    #Ahora a función da devolve o diccionario da contraseña
    return {
        "sistema" : nombre_plataforma ,
        "usuario" : nombre_usuario ,
        "seguridad" : nivel_seguridad ,
        "contraseña real" : password
    }
        
#Ahora toca facer o menu con todas as funciones
print(f"{VERDE}====================")
print(f"BIENVENIDO AL VAULT")
print(f"===================={RESET}")
while True:
    print(f"{VERDE}====================")
    print(f"{AMARILLO}1. {VERDE} Crear Contraseñas")
    print(f"{AMARILLO}2. {VERDE} Revisar sus Credenciales{RESET}")
    print(f"{AMARILLO}3. {VERDE} Salir del sistema guardando {RESET}")
    print(f"{VERDE}===================={RESET}")
    elecion = input(f"Que deseas hacer?: ")

    #Ahora hacemos las elecciones
    if elecion == '1' :
        print(f"{AMARILLO}CREADOR DE CONTRASEÑAS")
        print(f"====================")
        #Poner estas funciones sempre en una nova variable para asi poder añadir os returns donde me faga falta, ejemplo o 'nueva'
        nueva =crear_credenciales()

        caja_fuerte.append(nueva)

    elif elecion =='2' :
        print(f"{ROJO}\n🔑 --- TU EXPANSIÓN DE CREDENCIALES INDUSTRIALES ---{RESET}")
        if len(caja_fuerte) == 0 :
            print(f"Tu boveda esta vacía.")
        else :
            for cred in caja_fuerte :  #Creo que esta ben, ns de donde se sacao credencial/heroe
                sis = cred["sistema"]
                usu = cred["usuario"]
                seg = cred["seguridad"]
                real = cred["contraseña real"]

                #Funcionara ¿?
                llave_oculta = ocultar_llave(real)

                #Asignamos colores en base seg
                color_seg = VERDE if seg == "ALTA" else AMARILLO 
                #Curioso esta función quero aprender mais usos sobre esto

                #Ponemos las cosas en un print
                print(f"Sistema: {sis} | Usuario: {usu}")
                print(f"-> Seguridad: {color_seg}{seg}{RESET} | Llave: {llave_oculta}")
                print("---------------------------------------------")
    
    elif elecion == '3' :
        with open("caja_fuerte.json", "w" , encoding="utf-8") as f:
            json.dump(caja_fuerte, f, indent=4)
        print("El reporte fue guardado en caja_fuerte.json")
        print(f"{VERDE}Que tenga un buen dia")
        break

    
    
    #Salir y guardar perfecto
    else :
        print(f"{ROJO} La opción que pusiste no existe, vuelva a intentarlo.")


           
