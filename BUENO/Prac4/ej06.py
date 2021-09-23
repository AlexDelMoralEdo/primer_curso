def leer_lista_enteros():
    print('Ve introduciendo números enteros, o una cadena vacía para acabar...')
    numero = input('Nuevo número: ')
    enteros = []
    while numero != '':
        enteros += [int(numero)]
        numero = input('Nuevo número: ')
    return enteros

def borrar_elemento(lista_enteros, numero):
    contador = 0
    while contador < len(lista_enteros):
        if lista_enteros[contador] == numero:
            del lista_enteros[contador]
            return True
    return False



lista_enteros = leer_lista_enteros()
numero = int(input('¿Qué número debo eliminar de {}'.format(lista_enteros)))

while len(lista_enteros) > 0:
    if not borrar_elemento(lista_enteros, numero):
        print('Número no encontrado')
    if len(lista_enteros) == 0:
        break
    numero = int(input('¿Qué número debo eliminar de {}?'.format(lista_enteros)))

print('La lista ha quedado vacía')



