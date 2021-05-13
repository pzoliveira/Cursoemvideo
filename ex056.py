maiorih = -1
contmcmd20 = 0
media = 0
for cont in range(1, 5):
    print('----Dados da {}ª pessoa----'.format(cont))
    nome = str(input('Digite o nome: '))
    idade = int(input('Entre com a idade: '))
    sexo = str(input('Sexo [ M / F ]: '))
    media += idade / 4
    if sexo in 'Mn':
        if idade > maiorih:
            maiorih = idade
            nomehmv = nome
    else:
        if idade < 20:
            contmcmd20 += 1
    print('\n')
print('A idade média do grupo é {:.1f} anos.'.format(media))
if maiorih != -1:
    print('O homem mais velho do grupo chama-se {} e tem {} anos.'.format(nomehmv, maiorih))
if contmcmd20 !=0:
    print('Nesse grupo há {} mulheres com menos de 20 anos.'.format(contmcmd20))
