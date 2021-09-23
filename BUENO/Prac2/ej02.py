a = int(input('Introduce el número a: '))
b = int(input('Introduce el número b: '))
c = int(input('Introduce el número c: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('Es un triángulo')
else:
    print('No es un triángulo')

