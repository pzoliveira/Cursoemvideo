valores = list()
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    escolha = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if escolha in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse = True)
print(f'Os valores em ordem decrescentes são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
