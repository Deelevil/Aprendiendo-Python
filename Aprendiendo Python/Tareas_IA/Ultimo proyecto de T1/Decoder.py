#Ideas de proyecto, poder facer a codificación, osea poder darlle un texto normal e logo que se codifique

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

#Ahora temos que facer as def para poder compartelizar cada parte

def limpiar_contar(mensaje) :
    #Ahora facemos a función, temos que recibir o mensaje, cortar espacios, e contar palabras reales, como esto ultimo ni pta idea pero bueno
    snespacios = mensaje.strip()
    lpalabras = snespacios.split()  #Python sabe identificar que o parentesis vacio son varios espacios vacios, en vez de hard programalo para ser solo un espacio
    npalabras = len(lpalabras)
    return npalabras , snespacios
    #Deberia de estar pero seguro que esta mal, non comprendo estas novas funciones

def detectar_amenaza(mensaje) :
    #Mellora que teño que implementar, facer unha lista con todas as palabras prohibidas
    #Asi seria mais facil e simple comprobar e añadir novas entradas a o prohibido ou seguro.
    palabras_prohibidas = ["virus" , "hack" , "bomba" , "root"]
    #Facemos loop para poder recorrer toda a lista
    for palabra in palabras_prohibidas :
        if palabra in mensaje.lower() :
            return f"PELIGROSO (Detectado: {palabra})"
    #Este return activase se en todo o loop anterior non se activa
    return "SEGURO"
    

def desencriptar_codigo(mensaje) :
    #Esta e a parte na que facemos os .replace e podemos toquetear un pouco cos mensajes
    mensaje_desencriptado = mensaje.replace("4", "a").replace("3", "e").replace("1", "i").replace("0", "o")
    return mensaje_desencriptado

def encriptar_texto(mensaje) :
    cifrado = mensaje.lower().replace("a", "4").replace("e", "3").replace("i", "1").replace("o","0")
    return cifrado
    #función de cifrar lista

texto_limpio = ""

print(f"{AZUL}=============================================")
print(f"🕵️ CYBER-DECODER FORENSE v1.0 🕵️")
print(f"=============================================")
while True :
    print(f"=============================================")
    print(f"{AMARILLO}1.{AZUL} Interceptar y Limpiar Mensaje ")
    print(f"{AMARILLO}2.{AZUL} Analizar nivel de Amenaza ")
    print(f"{AMARILLO}3.{AZUL} Desencriptar Código ")
    print(f"{AMARILLO}4.{AZUL} Codificar Mensaje ")
    print(f"{AMARILLO}5.{ROJO} Salir.")
    print(f"{AZUL}============================================={RESET}")
    eleccion = input(f"Que deseas hacer?: ")
    print(f"{AZUL}============================================={RESET}")
    #Se que tengo todos estos if de forma erronea, no corrigas esto ya que se como hacerlos bien pero antes quiero saber si tengo bien los def.
    if eleccion == '1' :
        mensaje = input(f"{RESET}Introduzca el mensaje: ")
        n_palabras , texto_limpio = limpiar_contar(mensaje)
        #Ns que mas tendria que poner aquim no termino de comprender esta eleccion
        print(f"{AZUL} Este es el nº de palabras que tiene el texto:{n_palabras}")
        print(f"{AZUL} Y este es el texto interceptado:{RESET}{texto_limpio}")
        
    


    elif eleccion == '2' :
        if texto_limpio != "" :
            lector_amenaza = detectar_amenaza(texto_limpio)
            #Supongo que ya estaria lo que estaria aqui pedido
            if lector_amenaza == "SEGURO" :
                print(f"{VERDE}{lector_amenaza}{RESET}")
            else :
                print(f"{ROJO}{lector_amenaza}{RESET}")
        else :
            print(f"{ROJO}Debe seleccionar y limpiar un mensaje primero")

    

    

    elif eleccion == '3' :
        m_desencriptado = desencriptar_codigo(texto_limpio)
        #Deberia de funcionar???
        print(f"{AZUL} Mensaje desencriptado: {RESET}{m_desencriptado}")


    elif eleccion == '4' :
        #Codificación de mensajes normales
        texto_escrito = input(f"{RESET} Escriba a continuación el mensaje que desea encriptar: ")
        encriptado = encriptar_texto(texto_escrito)
        print(f"{RESET}{encriptado}")
    
    
    else :
        print(f"{VERDE} Que tenga un buen dia{RESET}")
        break