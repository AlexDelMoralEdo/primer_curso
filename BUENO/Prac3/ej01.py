#funciones
from math import pi
def área_círculo(r):
    return (pi*r**2)

def longitud_circunferencia(r):
    return (2*pi*r)

#programa principal

r= float(input('Introduce el radio: '))
print('Área: {:.2f}'.format(área_círculo(r)))
print('Longitud: {:.2f}'.format(longitud_circunferencia(r)))
