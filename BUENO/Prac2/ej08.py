a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))
c = int(input('Introduce el tercer número: '))
d = int(input('Introduce el cuarto número: '))

if a <= b and a <= c and a <= d:
    print('El menor es: {}'.format(a))
elif b <= c and b<=d:
    print('El menor es: {}'.format(b))
elif c <= d:
    print('El menor es: {}'.format(c))
else:
    print('El menor es: {}'.format(d))