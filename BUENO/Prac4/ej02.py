print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')
cadena = input('Nueva cadena: ')

lista_cadenas = []
lista_longitudes = []
cantidad_cadenas = 0
while cadena != '':
    lista_cadenas += [] + [cadena]
    longitud_cadena = len(cadena)
    lista_longitudes += [longitud_cadena]
    cantidad_cadenas += 1
    cadena = input('Nueva cadena: ')

print('Cadenas leídas (desde la última hasta la primera):')
for i in range(cantidad_cadenas-1, -1, -1):
    print('Cadena de longitud {}: =>{}<='.format(lista_longitudes[i], lista_cadenas[i]))
