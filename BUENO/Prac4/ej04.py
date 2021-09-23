def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')
    numero = input('Nuevo número: ')
    enteros = []
    while numero != '':
        enteros += [int(numero)]
        numero = input('Nuevo número: ')
    return enteros

#Programa principal
cuadrados = []
lista_enteros = leer_lista_enteros()
for i in range(len(lista_enteros)):
    cuadrado = lista_enteros[i] ** 2
    cuadrados += [cuadrado]
print('Cuadrados de los números leídos: {}'.format(cuadrados))
print('Números leídos: {}'.format(lista_enteros))




