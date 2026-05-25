def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0.0
    return sum(lista_notas)/len(lista_notas)

"""""
Esto hace que definamos la variable calcular_promedio tomando valores da lista de notas
Donde si no se tiene la lista te da el valor 0.0
Pero si tiene la lista te hace la operación matematica de Sumatorio de las notas/ El total de notas
"""