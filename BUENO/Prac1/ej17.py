a = int(input('Introduce a: '))
b = int(input('Introduce b: '))
c = int(input('Introduce c: '))


x1 = (-b + (b**2-4*a*c)**(1/2))/(2*a)
x2 = (-b - (b**2-4*a*c)**(1/2))/(2*a)

if (b**2-4*a*c) < 0:
    print('No existe solución para esa ecuación')
else:
    print('x1 = {}'.format(x1))
    print('x2 = {}'.format(x2))