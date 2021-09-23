primero = int(input('Introduce el primer número: '))
segundo = int(input('Introduce el segundo número: '))
tercero = int(input('Introduce el tercer número: '))

if primero <= segundo and primero <= tercero:
    print('El menor es: {}'.format(primero))

elif segundo <= tercero:
    print('El menor es: {}'.format(segundo))

else:
    print('El menor es: {}'.format(tercero))

