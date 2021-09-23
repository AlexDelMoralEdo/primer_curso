kwh = int(input('Introduce la cantidad de kWh: '))
importe = 0

if kwh <= 100:
    importe += kwh*0.05
    print('Importe: {:.2f} euros'.format(importe))

if kwh >100 and kwh <=250:
    importe += 100*0.05+(kwh-100)*0.07
    print('Importe: {:.2f} euros'.format(importe))

if kwh >250:
    importe += 100*0.05+150*0.07+(kwh-250)*0.1
    print('Importe: {:.2f} euros'.format(importe))


