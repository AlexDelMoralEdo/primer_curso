n = int(input('Introduce un número entero: '))

contador = 0
factorial = 1
while contador < n:
    contador += 1
    factorial *= contador

print('{}! = {}'.format(contador, factorial))


