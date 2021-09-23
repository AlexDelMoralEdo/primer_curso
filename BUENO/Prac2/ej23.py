n = int(input('Introduce un número entero: '))
suma = 0
i = 0

while i < n:
    i += 1
    if i % 3 != 0 and i % 5 != 0:
        suma += i
    else:
        suma = suma

print('La suma es {}'.format(suma))
