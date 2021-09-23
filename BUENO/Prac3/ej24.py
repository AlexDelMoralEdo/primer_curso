cadenaA = input('Introduce una cadena de caracteres A: ')
cadenaB = input('Introduce una cadena de caracteres B: ')

if cadenaB in cadenaA[len(cadenaA)-len(cadenaB):len(cadenaA)]:
    print('B es sufijo de A')
else:
    print('B no es sufijo de A')








