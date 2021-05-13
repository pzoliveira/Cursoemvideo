ladoa = float(input('Entre com o segmento a: '))
ladob = float(input('Entre agora com o segmento b: '))
ladoc = float(input('Finalmente digite o segmento c: '))
if ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
    possib = True
else:
    possib = False
if possib:
    if ladoa == ladob == ladoc:
        tipotri = 'EQÜILÁTERO'
    elif ladoa != ladob != ladoc != ladoa:
        tipotri = 'ESCALENO'
    else:
        tipotri = 'ISÓSCELES'
    print('Os segmentos PODEM formar um triângulo {}.'.format(tipotri))
else:
    print('Os segmentos NÃO podem formar um triângulo!!!!!!')
