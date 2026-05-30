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

clasificacion = []

try :
    with open("clasificacion.json","r") as f :
        clasificacion = json.load(f)
except FileNotFoundError :
    print("No se tiene un registro de flota")



print(f"{VERDE}================================")
print(f" Bienvenido a la arena jugador")
print(f"================================ {RESET}")

#RogueLike, no se gardan personajes


while True :

    #Ahora facemos o menu
    print(f"{ROJO}================================{RESET}")
    print(f"{AMARILLO}1.{RESET}{ROJO}Crear heroe: {RESET}")
    print(f"{AMARILLO}2.{RESET}{ROJO}Visualizar clasificaciones de los  heroes: {RESET}")
    print(f"{AMARILLO}3.{RESET}{ROJO}Combatir en la arena: ")
    print(f"{AMARILLO}4.{RESET}{ROJO}Salir: ")
    print(f"{ROJO}==================================={RESET}")
    decision = str(input(f"Que deseas hacer?: "))
    #Ahora as opciones
    if decision.lower() == '1' :
        print(f"{RESET}{AZUL}====================")
        print(f"Pantalla de generador de heroes")
        print(f"====================")
        nombre = input("Nombre del heroe: ")
        
        jugador = {
            "Nivel" :  0 ,
            "Nombre" : nombre ,
            "Vida" : 150 ,
            "Ataque" : 50 ,
            "Puntuacion" : 0 
        }
        print(f"Tu heroe fue creado con exito")
    if decision.lower() == '2' :
        print(f"{AMARILLO}====================")
        print(f" ---CLASIFICACIÓN---")
        print(f"====================")

        if len(clasificacion) == 0 :
            print(f"El marcador esta vacio, crea a tu primer heroe y a combatir")
        else:
            #Ordenamos el tablon
            clasificacion.sort(key=lambda jugador: jugador["Puntuacion"], reverse = True)

            for puesto , heroe in enumerate(clasificacion, start=1) : 
                nombre_c = heroe["Nombre"]
                nivel_c = heroe["Nivel"]
                punt_c = heroe["Puntuacion"]

                if puesto == 1 :
                    print(f"[1º PUESTO] {nombre_c} - {nivel_c} - {punt_c}")
                
                elif puesto == 2 :
                    print(f"[2º PUESTO] {nombre_c} - {nivel_c} - {punt_c}")
                elif puesto == 3 :
                    print(f"[3º PUESTO] {nombre_c} - {nivel_c} - {punt_c}")
                else :
                    print(f"{RESET} [{puesto}º PUESTO] {nombre_c} - {nivel_c} - {punt_c}")

            print(f"{AMARILLO}====================")
    

    if decision.lower() == '3' :
        #Ahora tenemos que poder generar un sistema de combate simple, con escaldo en base a oleadas y niveles
        #Ni puta idea de como empezar pero bueno malo sera
        if jugador is None :
            print(f"{ROJO}Debes de crear primero a un heroe en la Opción 1 {RESET}")
            continue

        #Ahora la entrada en el combate
        print(f"{ROJO}⚔️ ¡ENTRANDO A LA ARENA! ⚔️")
        ronda = 1  #Aqui tenemos a variable ronda
        vida_actual_j = jugador["Vida"] #Con esto generamos a nova variable para poder generar daño sin perder a vida maxima

        while True :
            print(f"\n{AMARILLO}--- OLEADA NUMERO {ronda} ---{RESET}")
            #Empezan os combates
            #Generamos enemigos (Aqui podremos en un futuro poder cambiar o tipo de enemigo en base a ronda)
            enemigo_01 = {
                "Nombre" : f"Goblin v.{ronda}" ,
                "Vida" : 0+(ronda*20.5) , #Al igual que el jugador, los enemigos escalan con el tiempo
                "Ataque" : 0+(ronda*10.5) ,
            }

            print(f" ¡Un {enemigo_01['Nombre']} ha aparecido !| (Vida :{enemigo_01['Vida']} | Ataque: {enemigo_01['Ataque']} )")

            #Ahora empeza o combate por turnos a muerte ( o primeiro que perda)
            while vida_actual_j > 0 and enemigo_01["Vida"] > 0 :
                input("[Presione ENTER para atacar]")
                #Ahora tenemos este input que solo hace que salte a la siguinte barra de codigo, por lo que se simulan los turnos consecutivos cada vez

                #Turno del jugador
                enemigo_01["Vida"] -= jugador["Ataque"]
                print(f"Le inflinges {jugador['Ataque']} de daño. Vida del enemgio: {enemigo_01['Vida']}")
                #Ahora la condicion de muerte del enemigo en nuestro turno
                if enemigo_01["Vida"] <= 0 :
                    print(f"Enemigo derrotado")
                    break
                
                #Turno del enemigo si a sobrevivido a nuestro turno
                vida_actual_j -= enemigo_01["Ataque"]
                print(f"El enemigo te ataca con {enemigo_01['Ataque']} de daño.Tu Vida: {vida_actual_j}")

            #Ahora hacemos el analisis de lo ocurrido en los turnos
            if vida_actual_j <= 0:
                print(f"\n{ROJO}💀 ¡HAS CAÍDO EN LA OLEADA {ronda}!{RESET}")
                #Calculamos la puntuacion final
                puntuacion_final = ronda * 250
                print(f"{AMARILLO}Puntuación obtenida: {puntuacion_final} puntos.{RESET}")
                

                #Ahora gardamos os datos na clasificación
                clasificacion.append({
                    "Nombre" : jugador["Nombre"] ,
                    "Nivel" : jugador["Nivel"] ,
                    "Puntuacion" : puntuacion_final
                })
                jugador = None
                break #Como perdiste se termina la partida
            else :
                print(f"{VERDE}¡Oleada {ronda} superada! Preparándose para el siguiente sector...{RESET}")
                ronda += 1 #Esto sinboliza el avance de rondas
                jugador["Nivel"] += 1
                jugador["Vida"] += 20
                jugador["Ataque"] += 10
                vida_actual_j = jugador["Vida"]
                print(f"{AZUL}-> ¡Subiste de nivel! Tu vida y ataque ahora son {jugador['Vida']} | {jugador['Ataque']}{RESET}")

    if decision.lower() == '4' :
        print(f"{VERDE}Que tenga un buen dia")
        with open("clasificacion.json", "w" , encoding="utf-8") as f:
            json.dump(clasificacion, f, indent=4)
        print("La clasificacion fue guardada en clasificacion.json")
        break

