def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')
    numero = input('Nuevo número: ')
    enteros = []
    while numero != '':
        enteros += [int(numero)]
        numero = input('Nuevo número: ')
    return enteros



lista_enteros = leer_lista_enteros()
posicion = int(input('¿Qué posición debo eliminar de {}'.format(lista_enteros)))

while len(lista_enteros) > 1:
    if posicion >= 0 and posicion < len(lista_enteros):
        del lista_enteros[posicion]
    else:
        print('Posición incorrecta')
    posicion = int(input('¿Qué posición debo eliminar de {}'.format(lista_enteros)))

print('La lista ha quedado vacía')


















