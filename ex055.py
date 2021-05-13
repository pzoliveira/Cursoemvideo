for cont in range(1, 6):
    peso = float(input('Entre com o peso da {}.a pessoa: '.format(cont)))
    if cont == 1:
        maior = menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('Menor {} e maior {}.'.format(menor, maior))
