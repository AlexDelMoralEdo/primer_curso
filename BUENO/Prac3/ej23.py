plantilla_correcta = input('Introduce la plantilla de respuestas correctas: ')
print('Ve introduciendo respuestas de alumnos, o vacío para acabar...')
respuestas = input('Nuevas respuestas: ')

alumnos = 0
while respuestas != '':
    if len(respuestas) != len(plantilla_correcta):
        print('La cadena introducida es de longitud {} (se esperaba {})'.format(len(respuestas), len(plantilla_correcta)))
        respuestas = input('Nuevas respuestas: ')
    else:
        bien = 0
        mal = 0
        ns = 0
        for pregunta in range(len(respuestas)):
            if respuestas[pregunta] == plantilla_correcta[pregunta]:
                bien += 1
            elif respuestas[pregunta] != '*':
                mal += 1
            else:
                ns += 1
        print('Resultados: {} BIEN; {} MAL; {} NS/NC'.format(bien, mal, ns))
        alumnos += 1
        respuestas = input('Nuevas respuestas: ')
print('Alumnos corregidos: {}'.format(alumnos))








