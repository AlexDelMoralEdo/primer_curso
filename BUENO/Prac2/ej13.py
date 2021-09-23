n = int(input('¿Cuántas veces prevés utilizar el gimnasio? '))

print('Con tarjeta: 50 euros.')

if n % 10 == 0:
    b = n // 10
    c_b = b * 20
    cbye = c_b
    print('Con bonos ({}): {} euros.'.format(b, c_b))
    print('Con bonos ({}) y entradas (0): {} euros.'.format(b, cbye))
else:
    b = n//10+1
    bb = n//10
    e = n % 10
    c_b = b * 20
    cbye = bb * 20 + e * 3
    print('Con bonos ({}): {} euros.'.format(b, c_b))
    print('Con bonos ({}) y entradas ({}): {} euros.'.format(bb, e, cbye))

c_t = 50

if c_t <= c_b and c_t <= cbye:
    recomendación = 'tarjeta.'
elif c_b <= cbye:
    recomendación = 'bonos.'
else:
    recomendación = 'bonos y entradas.'

print('Recomendación: {}'.format(recomendación))




