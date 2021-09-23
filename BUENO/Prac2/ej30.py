n = float(input('Introduce un número: '))
media = 0
contador = 0
suma = 0
máx = n
mín = n

if n < 0:
    print('No se han introducido datos')
else:
    while n >= 0:
        contador += 1
        suma += n
        media = suma / contador
        while n > máx:
            máx = n
        while n < mín:
            mín = n
        n = float(input('Introduce otro número: '))

    print('Media: {}'.format(media))
    print('Mínimo: {}'.format(mín))
    print('Máximo: {}'.format(máx))

