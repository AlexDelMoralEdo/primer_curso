#funcion
def contar_secuencias_dígitos(cadena):
    secuencias = 0
    nuevo_digito = True
    for caracter in cadena:
        if caracter in '1234567890':
            if nuevo_digito:
                secuencias += 1
                nuevo_digito = False
        else:
            nuevo_digito = True
    return secuencias


#Programa principal
print('Ve introduciendo cadenas de caracteres, o vacío para acabar...')
cadena = input('Nueva cadena: ')
while cadena != '':
    print('Secuencias de dígitos encontradas: {}'.format(contar_secuencias_dígitos(cadena)))
    cadena = input('Nueva cadena: ')
print('¡Adiós!')


