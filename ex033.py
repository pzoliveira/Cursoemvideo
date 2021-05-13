prival = int(input('Primeiro valor: '))
seval = int(input('\nSegundo valor: '))
terval = int(input('\nTerceiro valor: '))
if prival > seval:
    if prival > terval:
        maior = prival
        menor = seval if seval < terval else terval
    else:
        maior = terval
        menor = seval
else:
    if seval > terval:
        maior = seval
        menor = prival if prival < terval else terval
    else:
        maior = terval
        menor = prival
print('\nO maior valor é {}'.format(maior))
print('\nO menor valor é {}'.format(menor))