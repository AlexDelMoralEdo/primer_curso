import math

Lado1 = float(input('Introduce el primer lado: '))
Lado2 = float(input('Introduce el segundo lado: '))
Ángulo_radianes = float(input('Introduce el ángulo (en grados): '))

Ángulo_grados = Ángulo_radianes*math.pi/180

Área = (1/2)*Lado2*Lado1*math.sin(Ángulo_grados)

print('El área del triángulo es: {:.2f}'.format(Área))
