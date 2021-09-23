print('Ve introduciendo números enteros positivos, o un número negativo para acabar...')
numero = int(input('Nuevo número: '))

pares = []
impares = []
while numero >= 0:
    if numero % 2 == 0:
        pares += [numero]
    else:
        impares += [numero]
    numero = int(input('Nuevo número: '))
print('Números pares: {}'.format(pares))
print('Números impares: {}'.format(impares))

