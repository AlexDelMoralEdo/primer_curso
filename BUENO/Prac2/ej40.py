n = int(input('Introduce un número entero: '))
print('Los {} primeros números primos son: '.format(n), end='')

primos = 1
contador = 1
primo = True
while primos <= n:
    primo = True
    contador += 1
    for divisor in range(2, contador):
        if contador % divisor == 0:
            primo = False
    if primo:
        print(contador, end=' ')
        primos += 1








