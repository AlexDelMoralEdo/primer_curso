def ola_frio_mas_larga(temperaturas):
    #Calcula y devuleve el comienzo y la duracion de la ola de frio mas larga
    #Consideramos como frio, cuando la temperatura es negativa
    comienzo = 0
    longitud = 0
    comienzo_ola_mas_larga = 0
    longitud_ola_mas_larga = 0
    for i in range(len(temperaturas)):
        if temperaturas[i] < 0:
            longitud += 1
        else:
            if longitud > 0:
                print('comienzo = {} longitud = {}'.format(comienzo, longitud))
            comienzo = i + 1   #suponemos que el siguiente dia es una ola de frio(no afecta a la buclefor)
            longitud = 0

    if longitud > 0:  #si no anyadimos esta parte, daria error al acabar en ola de frio
        print('comienzo = {} longitud = {}'.format(comienzo, longitud))
    if longitud > longitud_ola_mas_larga:
        comienzo_ola_mas_larga = comienzo
        longitud_ola_mas_larga = longitud
    return [longitud_ola_mas_larga, comienzo_ola_mas_larga]


#Programa principal
enero = [14, 5, -3, -1, -4, 4, 8, -5, -6, -7, -3, 3, 4, -1, 8, 10]
[comienzo_ola, longitud_ola] = ola_frio_mas_larga(enero)
print('La ola de frio mas larga empezo el dia {0} y duro {1} dias'.format(comienzo_ola, longitud_ola))
