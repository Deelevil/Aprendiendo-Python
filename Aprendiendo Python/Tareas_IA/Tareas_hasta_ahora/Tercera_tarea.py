# Tercera tarea: Importar funciones desde otro archivo
# En esta tarea, vamos a importar funciones desde otro archivo llamado geometria.py
#Se usa con el comando from, para seleccionar el archivo y luego la función import para seleccionar las variables que queremos importar
# Se usa el comando try-except para manejar posibles errores, como ingresar un valor no numérico o intentar dividir por cero. Esto hace que el programa sea más robusto y fácil de usar.
from geometria import area_circulo, division_segura
try:
    r=float(input("Cual es el radio del circulo?"))
    print(f"El área del círculo es: {area_circulo(r):.2f}")
    n1=float(input("Ingrese el primer nº de la división:"))
    n2=float(input("Ingrese el segundo nº de la división:"))
    print(f"El resultado de la división es: {division_segura(n1,n2)}")

except ValueError: #Esto captura errores de tipo de dato, como ingresar texto en lugar de números
    print("Error: Por favor ingrese un número válido.")
except ZeroDivisionError: #Esto captura errores de división por cero, aunque en este caso la función division_segura ya maneja ese error, es una medida adicional
    print("Error: No se puede dividir por cero.")
else: #Esto se ejecuta si no hay errores, es opcional pero puede ser útil para confirmar que el programa se ejecutó correctamente
    print("Operaciones realizadas con éxito.")
finally: #Esto se ejecuta siempre, independientemente de si hubo errores o no, es útil para limpiar recursos o simplemente para indicar que el programa ha terminado
    print("Gracias por su uso.")
