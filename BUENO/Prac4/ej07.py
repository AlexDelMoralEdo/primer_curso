def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')
    numero = input('Nuevo número: ')
    enteros = []
    while numero != '':
        enteros += [int(numero)]
        numero = input('Nuevo número: ')
    return enteros


def borrar_elemento(lista_enteros, numero):
    contador = len(lista_enteros) - 1
    while contador >= 0:
        if lista_enteros[contador] == numero:
            del lista_enteros[contador]
            return True
        contador -= 1
    return False

lis_enteros = leer_lista_enteros()


while len(lis_enteros) > 0:
    numero = int(input('¿Qué número debo eliminar de {}? '.format(lis_enteros)))
    if not borrar_elemento(lis_enteros, numero):
        print('Número no encontrado')
    if len(lis_enteros) == 0:
        break

print('La lista ha quedado vacía')

