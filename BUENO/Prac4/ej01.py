print('Ve introduciendo cadenas de caracteres, o vacio para acabar...')
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

print('Cadenas leidas: ')

for i in range(cantidad_cadenas):
    print('Cadena de longitud {}: =>{}<='.format(lista_longitudes[i], lista_cadenas[i]))
