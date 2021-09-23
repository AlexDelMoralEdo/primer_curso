#Función

def es_triángulo(a,b,c):
    if a<(b+c) and b<(c+a) and c<(b+a):
        triángulo = True
    else:
        triángulo = False
    return triángulo

#programa principal

a = int(input('Introduce el número a: '))
b = int(input('Introduce el número b: '))
c = int(input('Introduce el número c: '))

if es_triángulo(a,b,c):
    print('Es un triángulo')
else:
    print('No es un triángulo')