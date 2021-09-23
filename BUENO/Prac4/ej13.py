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

def posición_menor(lista_enteros, desde_contar):
    contador = desde_contar
    menor = lista_enteros[contador]
    posicion = contador
    while contador < len(lista_enteros):
        if lista_enteros[contador] < menor:
            menor = lista_enteros[contador]
            posicion = contador
        contador += 1
    return posicion

def intercambiar(lista_enteros, i, j):
    pos_auxiliar = lista_enteros[j]
    lista_enteros[j] = lista_enteros[i]
    lista_enteros[i] = pos_auxiliar

def ordenar_lista(lista_enteros):
    primer_num = 0
    while primer_num < (len(lista_enteros) - 1):
        pos_menor = posición_menor(lista_enteros, primer_num)
        intercambiar(lista_enteros, primer_num, pos_menor)
        primer_num += 1
    return lista_enteros



lista_enteros = leer_lista_enteros()
print('Lista leída: {}'.format(lista_enteros))
ordenar_lista(lista_enteros)
print('Lista ordenada: {}'.format(lista_enteros))
