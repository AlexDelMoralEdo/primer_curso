primero = int(input('Introduce el primer número: '))
segundo = int(input('Introduce el segundo número: '))

if primero == segundo:
    print('Los dos número son iguales')
else:
    if primero < segundo:
        print('El menor es: {}'.format(primero))
    else:
        print('El menor es: {}'.format(segundo))

