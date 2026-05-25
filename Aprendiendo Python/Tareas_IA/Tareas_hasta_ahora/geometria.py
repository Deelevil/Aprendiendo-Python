import math #Sirve para importar funciones matemáticas, como pi y sqrt
def area_circulo(radio):  #Función para calcular el área de un círculo
    return math.pi * radio ** 2 #La fórmula para el área de un círculo es A = πr²

def division_segura(a,b):
    if b == 0:
        return "Error: División por cero"
    return a / b

