listanum = list()
while True:
    num = int(input('Digite um número para se adicionado a uma lista: '))
    if num in listanum:
        print('Número duplicado! NÃO foi adicionado!!!')
    else:
        listanum.append(num)
        print('Número adicionado com sucesso!!!')
    escolha = 'a'
    while escolha not in 'nNsS':
        escolha = str(input('Deseja adicionar mais números? [S/N] ')).strip()[0]
    if escolha in 'nN':
        break
print(f'Você digitou os valores {sorted(listanum)}')
