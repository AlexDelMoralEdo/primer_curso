#FUNCIONES
def es_letra_castellana(caracter):
    letra = True
    letra_min = caracter.lower()
    if not (letra_min >= 'a' and letra_min <= 'z' or letra_min in 'ñüáéíóú'):
        letra = False
    return letra

def primer_no_castellano(palabra):
    for caracter in palabra:
        if not es_letra_castellana(caracter):
            return caracter



#Programa principal

print('Ve introduciendo palabras, o vacío para acabar... ')
palabra = input('Nueva palabra: ')
while palabra != '':
    if primer_no_castellano(palabra) is None:
        print('podría ser una palabra correcta')
    else:
        print('Contiene un carácter que no es del alfabeto castellano: \'{}\''.format(primer_no_castellano(palabra)))
    palabra = input('Nueva palabra: ')
print('¡Adiós!')