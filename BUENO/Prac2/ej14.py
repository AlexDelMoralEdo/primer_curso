importe = float(input('Introduce el importe de la compra: '))

zona = input('Introduce la zona de envío (A/B/C): ')
socio = input('¿Eres socio (S/N)? ')

if importe <= 150:
    if socio == 'N':
        gastos = 25
    else:
        gastos = 19
if importe > 150.01 and importe <= 750.01:
    if socio == 'N':
        gastos = 60
    else:
        gastos = 49
if importe > 750.01 and importe <= 1500:
    if socio == 'N':
        gastos = 120
    else:
        gastos = 89
if importe > 1500:
    if socio == 'N':
        gastos = importe * (8 / 100)
    else:
        gastos = importe * (6 / 100)

if zona == 'B':
    gastos = gastos + 30
if zona == 'C':
    gastos = gastos + 69

print('Gastos de envío: {:.2f} euros'.format(gastos))


