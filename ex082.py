listanum = list()
while True:
    listanum.append(int(input('Digite um número: ')))
    escolha = input('Quer continuar? [S/N] ')
    if escolha in 'Nn':
        break
print(f'A lista completa é {listanum}')
listapar = list()
listaimpar = list()
for elem in listanum:
    if elem % 2 == 0:
        listapar.append(elem)
    else:
        listaimpar.append(elem)
print(f'A lista de elementos pares é {listapar}')
print(f'A lista de elementos ímpares é {listaimpar}')
