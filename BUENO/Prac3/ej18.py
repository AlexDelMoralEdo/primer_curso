#Funciones

def analizar_digitos(cadena):
    todo_digitos = True
    suma_elementos = 0
    for elemento in range(len(cadena)):
        if cadena[elemento] not in '1234567890':
            todo_digitos = False
            no_digito = cadena[elemento]
            break
        else:
            suma_elementos += int(cadena[elemento])
    if todo_digitos:
        print('Todos los caracteres son dígitos')
        print('¿Cuántos dígitos? {}'.format(len(cadena)))
        print('¿Suma de dígitos? {}'.format(suma_elementos))
    else:
        print('Primer "no dígito": \'{}\' en posición {}'.format(no_digito, elemento))





#Programa principal

cadena = input('Introduce una cadena de caracteres: ')
analizar_digitos(cadena)


