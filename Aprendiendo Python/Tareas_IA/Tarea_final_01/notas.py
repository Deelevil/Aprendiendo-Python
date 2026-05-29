#Ten posibles melloras. A IA xa me esta mandando a facer novas cousas pero quero probar se funciona
    #Error: Si ingresamos un error no nos permite poder repetir el proceos
    #La lista no es visual, no se puede ver el resultado de las notas, materias y promedios
    #Podemos hacer un sistema de menu para poder elegir entre ingresar datos, ver datos, exportar datos, etc.
import json

from calculos import calcular_promedio

#Ahora hacemos la lista de los estudiantes con sus nombres, materias y notas
estudiantes = []
materias_unicas = set()
#Creo que poderia facer outro loop para poder añadir mais estudantes.
try:
    with open("estudiantes.json", "r") as f:
         estudiantes = json.load(f)
except FileNotFoundError:
        print("No se encontró el archivo estudiantes.json. Se creará uno nuevo al guardar los datos.")

while True:
    nombre = input("Ingrese el nombre del siguiente estudiante (o 'salir' para termianr):")
    if nombre.lower() == 'salir':
        break
    try:
        n = int (input("Ingrese el número de materias:"))
        registro_estudiantex = {}
        #Este diccionario deberia de funcionar ¿¿??
        #Hacemos un ciclo for para ingresar las materias y notas de cada estudiante, donde antes definimos cuantos ciclos tiene que hacer con la varibale n.
        for i in range(n):
            materia = input("Ingrese el nombre de la materia {}:".format(i+1))
            nota = float (input("Ingrese su nota de la materia {}:".format(i+1)))
            materias_unicas.add(materia)
            registro_estudiantex[materia]=nota
        # Ahora que tenemos el diccionario, actualizamos e gardamos os datos na variable registro_estudiantex
        #Todo o de arriba esta actualozado con o novo sistema de diccionario de estudiantes. 

        #Ahora calculamos el promedio, esto deberia de funcionar.
        notas_num= list(registro_estudiantex.values())
        promedio_final =calcular_promedio(notas_num)

        #Ahora necesitamos gardar os datos en forma de expediente completo con todos os datos.
        #Incluindo obv. nombre,materias,notas e o promedio.
        estudiantes.append({
        "nombre":nombre,
        "materias":registro_estudiantex,
        #Por que no se pone las notas? Es por que ya estan dentro del registro_estudiantex
        "promedio":promedio_final
        })
        #Esta todo perfecto ahora solo falta cerrar o try
    except ValueError:
        print("Error: Debes ingresar un nº para el nº de materias y para las notas.")
    except Exception as e:
        print("Ocurrió un error inesperado:", str(e))
#Ter en conta as barritas da izquierda.
#Ahora facemos a exportación dos datos a archivos para poder gardalos

exportar = input("¿Desea exportar los datos a un archivo JSON? (s/n):")
if exportar.lower() == 's':
      with open("estudiantes.json", "w") as f:
        json.dump(estudiantes, f, indent=4)
        print("Datos exportados a estudiantes.json")
else:
    print("Exportación cancelada.") 

#Terminado esta vez si
