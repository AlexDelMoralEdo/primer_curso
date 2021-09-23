def mostrar_cadena_repetida(c,n,s):
     print((c+s)*(n-1)+c)

#Programa

c = input('Introduce una cadena: ')
s = input('Introduce un separador: ')
m = int(input('Introduce un máximo de repeticiones: '))

contador = 1
n = 1
while contador <= m:
    contador += 1
    mostrar_cadena_repetida(c,n,s)
    n += 1
