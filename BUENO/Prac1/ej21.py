from math import pi

def área_círculo(radio):
    return pi*radio**2

radio = float(input('Introduce el radio: '))

print('Área: {}'.format(área_círculo(radio)))
