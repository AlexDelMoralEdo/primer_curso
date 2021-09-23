def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')
    numero = input('Nuevo número: ')
    enteros = []
    if numero == '':
        return enteros
    while numero != '':
        enteros += [int(numero)]
        numero = input('Nuevo número: ')
    return enteros

def posición_menor(lista_enteros):
    contador = 0
    menor = lista_enteros[contador]
    posicion = 0
    while contador < len(lista_enteros):
        if lista_enteros[contador] < menor:
            menor = lista_enteros[contador]
            posicion = contador
        contador += 1
    return posicion

def intercambiar(lista_enteros, j, i):
    pos_auxiliar = lista_enteros[j]
    lista_enteros[j] = lista_enteros[i]
    lista_enteros[i] = pos_auxiliar


lista_enteros = leer_lista_enteros()

if len(lista_enteros) == 0:
    print('Lista leída: {}'.format(lista_enteros))
    print('Modificada: {}'.format(lista_enteros))
else:
    print('Lista leída: {}'.format(lista_enteros))
    i = posición_menor(lista_enteros)
    j = 0
    if lista_enteros[i] != lista_enteros[j]:
        intercambiar(lista_enteros, j, i)
    print('Modificada: {}'.format(lista_enteros))






