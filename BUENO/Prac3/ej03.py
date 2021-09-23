#función
def es_triángulo(a,b,c):
    return a < (b+c) and b < (c+a) and c < (b+a)

def tipo_triángulo(a, b, c):
    if es_triángulo(a, b, c):
        if a == b and b == c:
            return 'equilátero'
        elif a == b !=c or a == c !=b or b == c != a:
            return 'isósceles'
        elif a != b != c != a:
            return 'escaleno'
    else:
        return None


#Programa principal

a = int(input('Introduce el lado a: '))
b = int(input('Introduce el lado b: '))
c = int(input('Introduce el lado c: '))

while tipo_triángulo(a, b, c) is None:
    print('No es un triángulo')
    a = int(input('Introduce el lado a: '))
    b = int(input('Introduce el lado b: '))
    c = int(input('Introduce el lado c: '))

print('Es {}'.format(tipo_triángulo(a,b,c)))



