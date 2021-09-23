n = int(input('Introduce un número entero: '))

print('Los números primos menores que {} son:'.format(n), end=' ')

for candidato in range(2, n):
    primo = True
    for divisor in range(2, candidato):
        if candidato % divisor == 0:
            primo = False
    if primo:
        print(candidato, end=' ')




