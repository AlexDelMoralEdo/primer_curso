Lado1 = float(input('Introduce el primer lado: '))
Lado2 = float(input('Introduce el segundo lado: '))
Ángulo = float(input('Introduce el ángulo (en radianes): '))

from math import sin

Área = (1/2)*Lado2*Lado1*sin(Ángulo)

print('El área del triángulo es: {:.2f}'.format(Área))







