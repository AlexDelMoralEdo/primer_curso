# coding=utf-8

def triplicar(lista_numeros):
    #Multilpica por 3 a lista original
    for i in range (len(lista_numeros)):
        lista_numeros[i]*= 3


def triplicada(lista_numeros):
    #Devuelve una NUEVA lista multiplicada por 3
    resultado = [0] * len(lista_numeros)
    for i in range(len(lista_numeros)):
        resultado[i] = lista_numeros[i] * 3
    return resultado


#Program principal
lista_a = [1, 2, 3, 4]
print('Antes de llamara triplicar, lista_A = {}'.format(lista_a))
triplicar(lista_a)
print('Después de llamar a triplicar, lista_a = {}'.format(lista_a))
