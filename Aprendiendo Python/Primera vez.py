
print("Hello World")
print("Vamos a por todas esta vez")
5+5 
#Podo escribir o que queira aqui, pero no se ejecutará nada, porque no es código, sino texto.
# Esto es un comentario, no se ejecutará nada, pero sirve para explicar el código a los demás o a nosotros mismos en el futuro.
# Esto es un comentario de una sola línea

"""
Esto es un comentario de varias líneas
que se puede escribir entre comillas triples. Todo lo que esté entre las comillas triples se considerará un comentario y no se ejecutará.

"""
# Esto es un comentario de varias líneas también, pero con el símbolo de almohadilla al principio de cada línea

[[1+2], [3+4], [5+6]]
# Esto es una lista de listas, cada una con una operación matemática dentro. Se ejecutará cada operación y se mostrará el resultado en una lista de listas.

#Vamos probar o que nos dixo Gemini
presupuesto = input("Cuanto dinero tienes ahorrado para el mac mini?")

#El input siempre lee texto, si queremos un nº necesitamos int (nº entero) o float (nº con decimales)
presupuesto_num = int(presupuesto)

# Ahora que tenemos valores numericos con el presupuesto, podemos hacer calculos.
cuanto_falta = 999 - presupuesto_num

#Ahora podemos mostrar el resultado al usuario
print("Te faltan exactamente " + str(cuanto_falta) + " euros para comprar el mac mini")

# Si ponemos comas , en lugar de +, el resultado se mostrará con espacios entre los elementos, lo que puede ser más legible.
print("Te faltan exactamente", cuanto_falta, "euros para comprar el mac mini")
#Y seria la misma cosa

#Vamos a jugar con los if
if presupuesto_num < 999 and presupuesto_num >= 100 :
    print("Aún te falta dinero para comprar el mac mini, exactamente" , cuanto_falta, "euros")
elif presupuesto_num >=999 and presupuesto_num < 1500 :
    print("Ya tienes suficiente dinero ahorrado para comprar un mac mini.")
else :
    print("Tienes que conseguir mas dinero", presupuesto_num, "euros es muy poco, eres un pobre de mierda")

#Ahora que xa xogeui con print, input, str e if, vamos a probar con los bucles for.
#Para eso necesitamos una lista, vamos a crear una lista de objetivos de tiempo
mis_objetivos = [
    ["Aprender Python",2026,7,31],
    ["Aprender a usar Github",2026,7,30],
    ["Aprender a usar Obsidian",2026,6,30],
    ["Aprender a aprovechar la IA",2026,9,1]
]
#Ahora temos unha lista cos meus objetivos, dentro da variable mis_objetivos,
#Ahora vamos poñer a formula para facer sort 
mis_objetivos.sort(key=lambda x: (x[1], x[2], x[3]))

# Cada objetivo é unha lista con dúas partes, o nome do obxetivo e a data límite para conseguilo.
#Agora podemos usar un bucle for para mostrar cada obxetivo e a súa data
print("-----Objetivos ordenados por data límite-----")
for objetivo in mis_objetivos:
    print("Mi proximo objetivo es", objetivo[0], "y tengo hasta el", objetivo[1],"/", objetivo[2],"/", objetivo[3], "para conseguirlo.")
