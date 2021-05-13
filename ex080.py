listanum = ['a', 'a', 'a', 'a', 'a']
for cont in range(5):
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = num
        listanum.append(num)
        print('Adicionado ao final da lista...')
    else:
        if num > maior:
            listanum.append(num)
            print('Adicionado ao final da lista...')
            maior = num
        else:
            pos = 0
            for cont in range(len(listanum)):
                if listanum[cont] != 'a':
                    if num < listanum[cont]:
                        break
                    else:
                        pos += 1
            listanum.insert(cont, num)
            print(f'Adicioando na posição {pos} da lista...')
print('-=' * 31)
for apa in range(listanum.count('a')):
    listanum.remove('a')
print(f'Os números digitados em ordem crescente foram {listanum}')
