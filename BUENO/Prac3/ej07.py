#Función
def contar_divisores(x):
    divisores = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisores += 1
    return divisores




#Programa principal
n = int(input('Introduce un número entero: '))

mayor = 1
divisores_de_mayor = 1
for i in range(1, n+1):
    if contar_divisores(i) >= divisores_de_mayor:
        mayor = i
        divisores_de_mayor = contar_divisores(i)

print('El número con más divisores es {} ({} divisores)'.format(mayor, divisores_de_mayor))


