import json
# Cargar el archivo JSON

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True
#Definir la función para verificar si un número es primo

#Ahora haremos la lista de números primos utilizando la función es_primo
lista_primos=[]

#Ahora hacemos el circulo try except para cargar el archivo JSON
try:
    #1º la lectura del archivo JSON
    with open("C:\\Users\\xiane\\Desktop\\Python\\Aprendiendo Python\\Tareas_IA\\datos.txt","r") as archivo: #Asegúrate de colocar la ruta correcta del archivo datos.txt
        lineas=archivo.readlines()
        for linea in lineas:
            num=int(linea.strip()) #Convertimos la línea a un número entero
            if es_primo(num): #Verificamos si el número es primo
                lista_primos.append(num) #Si es primo, lo añadimos a la lista de primos

    #2º Es la creación del reporte
    reporte={
    "resultados primos":lista_primos,
    "cantidad encontrada":len(lista_primos)
}

    #3º Es la escritura del reporte en un nuevo archivo JSON
    with open("reporte_primos.json","w") as json_file:
        json.dump(reporte,json_file,indent=4)
        print("Reporte JSON generado exitosamente.")

except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no se encontró.")
except ValueError:
    print("Error: El archivo contiene datos que no son números validos.")

#Terminado.