# coding=utf-8
from random import randint, random
print('Voy a pensar un número del 1 al 10...')
numero = int(input('Intenta adivinar el numero: '))
numero_pensado = randint(1,10)

while numero != numero_pensado:
    numero = int(input('Vaya, has fallado. Prueba de nuevo: '))
print('Enhorabuena, lo has certado.')




