#Funciones
def leer_entero_mayor_que(n):
    a = int(input('Introduce un entero mayor que {}: '.format(n)))
    while a <= n:
        a = int(input('Esperaba entero mayor que {} y {} no lo es. Dame otro: '.format(n, a)))
    return a


def contar_divisores(x):
    div = 0
    for divisor in range(1, x+1):
            if x % divisor == 0:
                div += 1
    return div



def es_primo(div):
    if contar_divisores(div) == 2:
        return True
    else:
        return False


#Programa principal
x = leer_entero_mayor_que(0)
y = leer_entero_mayor_que(x)
print('Voy a buscar primos entre {} y {}...'.format(x, y))
print('Encontrados: ', end='')

primos = 0
for candidato in range(x, y+1):
    if es_primo(candidato):
        primos += 1
        print(candidato, end=' ')
if primos == 0:
    print('Ninguno')




