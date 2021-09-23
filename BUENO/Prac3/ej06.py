#Función
def contar_divisores(n):
    div = 0
    for i in range(1, n+1):
        if n % i == 0:
            div += 1
    return div

#Programa principal

n = int(input('Introduce un número entero: '))
print('El número {} tiene {} divisores'.format(n, contar_divisores(n)))


