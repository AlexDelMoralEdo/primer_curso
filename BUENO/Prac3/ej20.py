#FUNCIONES
def es_palabra_castellana(palabra):
    palabra_castellana = True
    for letra in palabra:
        letra_min = letra.lower()
        if not (letra_min >= 'a' and letra_min <= 'z' or letra_min in 'ñüáéíóú'):
            palabra_castellana = False
            break
    if palabra_castellana:
        print('Podría ser una palabra correcta')
    else:
        print('Contiene un carácter que no es del alfabeto castellano: \'{}\''.format(letra))





#Programa principal

print('Ve introduciendo palabras, o vacío para acabar... ')
palabra = input('Nueva palabra: ')
while palabra != '':
    es_palabra_castellana(palabra)
    palabra = input('Nueva palabra: ')
print('¡Adiós!')