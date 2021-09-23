a = int(input('Introduce un ángulo (en grados): '))
if a == 0:
    print('Nulo')
elif a < 90:
    print('Agudo')
elif a == 90:
    print('Recto')
elif a < 180:
    print('Obtuso')
elif a == 180:
    print('Llano')
elif a < 360:
    print('Cóncavo')
elif a == 360:
    print('Completo')
else:
    print('No existe tal ángulo')


