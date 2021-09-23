#Función
def sumar_divisores_propios(n):
    suma_div = 0
    for i in range(1,n):
        if n % i == 0:
            suma_div += i
    return suma_div

def es_abundante(n):
    if n < sumar_divisores_propios(n):
        return True
    else:
        return False




#Program principal
n = int(input('Introduce un número entero: '))
print('Los números abundantes menores que {} son: '.format(n), end='')

candidato = 0
abundantes = 0

while candidato < (n-1):
    candidato += 1
    if es_abundante(candidato):
        print(end=' {}'.format(candidato))


