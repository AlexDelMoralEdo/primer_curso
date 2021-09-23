a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))

if a*b < 0:
    print('Su producto es negativo')
elif a*b >0:
    print('Su producto es positivo')
else:
    print('Su producto es nulo')