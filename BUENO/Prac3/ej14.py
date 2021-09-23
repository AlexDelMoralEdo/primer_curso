cadena = input('Introduce un texto (vacío para acabar): ')

if cadena == '':
    print('No se ha introducido ningún texto')
else:
    min = len(cadena)
    cadena_min = cadena

    max = len(cadena)
    cadena_max = cadena

    while len(cadena) > 0:
        cadena = input('Introduce otro texto (vacío para acabar): ')
        if len(cadena) <= min and len(cadena) != 0:
            min = len(cadena)
            cadena_min = cadena
        if len(cadena) >= max:
            max = len(cadena)
            cadena_max = cadena
    print('Última cadena de mínima longitud, {}: =>{}<='.format(min, cadena_min))
    print('Última cadena de máxima longitud, {}: =>{}<='.format(max, cadena_max))