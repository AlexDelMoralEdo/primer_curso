n = int(input('Introduce un número entero: '))

i = 0
divisores = 0

while i < n:
    i += 1
    if n % i == 0:
        divisores += 1
    else:
        divisores = divisores

print('El número {} tiene {} divisores'.format(n, divisores))



