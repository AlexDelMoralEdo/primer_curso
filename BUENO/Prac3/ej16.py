def analizar_digitos(cadena):
    todo_digitos = True
    for elemento in cadena:
        if elemento not in '1234567890':
            todo_digitos = False
    return todo_digitos


cadena = input('Introduce una cadena de caracteres: ')
if analizar_digitos(cadena):
    print('Todos los caracteres son dígitos')
else:
    print('No todos los caracteres son dígitos')





