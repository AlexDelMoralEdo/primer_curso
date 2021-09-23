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

def repetidos_lista(lista_enteros):
    contador = 0
    lista_repetidos = []
    while contador < len(lista_enteros):
        posible_repetido = lista_enteros[contador]
        for i in range(contador + 1, len(lista_enteros)):
            if posible_repetido == lista_enteros[i] and posible_repetido not in lista_repetidos:
                lista_repetidos += [posible_repetido]
        contador += 1
    return lista_repetidos

def suma_lista(lista_repetidos):
    suma = 0
    for i in range(len(lista_repetidos)):
        suma += lista_repetidos[i]
    return suma


lista_enteros = leer_lista_enteros()
lista_repetidos = repetidos_lista(lista_enteros)
suma_repetidos = suma_lista(lista_repetidos)
print('Números leídos más de una vez (suman {}): {}'.format(suma_repetidos, lista_repetidos))
print('Todos los números leídos: {}'.format(lista_enteros))
