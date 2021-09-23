n = int(input('Introduce un número entero: '))

contador = 0
cuadrado = 0

while (contador+1)**2 < n:
    contador += 1
    cuadrado = contador**2
    print('El cuadrado de {} es {}'.format(contador, cuadrado))