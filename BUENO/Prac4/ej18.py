from aetypes import end

import aetypes.end

def crear_matriz_ceros(num_filas, num_columnas):
    # Creamos la matriz de num_filas x num_columnas ceros
    matriz = []
    for i in range(num_filas):
        matriz.append([0.0] * num_columnas)
    return matriz


def leer_matriz(num_filas, num_columnas):
    matriz = crear_matriz_ceros(num_filas, num_columnas)
    for i in range(num_filas):
        for j in range(num_columnas):
            matriz[i][j] = float(input('  elemento ({}, {}): '.format(i, j)))
    return matriz


def mostrar_matriz(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    for i in range(num_filas):
        for j in range(num_columnas):
            print('{:7.2f}'.format(matriz[i][j]), end=' ')
        print()


# Programa principal
print('Lectura de la matriz')
filas = int(input('  número de filas:    '))
columnas = int(input('  número de columnas: '))

m = leer_matriz(filas, columnas)
print('La matriz leída es....')
mostrar_matriz(m)