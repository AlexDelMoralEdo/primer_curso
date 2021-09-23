a = int(input('Introduce el lado a: '))
b = int(input('Introduce el lado b: '))
c = int(input('Introduce el lado c: '))

while not a < (b+c) or not b < (a+c) or not c < (a+b):
    print('No es un triángulo')
    a = int(input('Introduce el lado a: '))
    b = int(input('Introduce el lado b: '))
    c = int(input('Introduce el lado c: '))


if a == b == c:
    print('Es equilátero')
elif a == b != c or a == c != b or b == c != a:
       print('Es isósceles')
else:
    print('Es escaleno')






