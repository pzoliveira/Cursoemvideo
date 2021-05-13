num = int(input('Digite um número inteiro qualquer positivo diferente de zero: '))
indica = 0
vezes = 0
for cont in range(1, num +1):
    indica = 1 if num % cont == 0 else 0
    vezes += indica
    print('\033[33m' if indica ==1 else '\033[31m', end = ' ')
    print('{}'.format(cont), end=' ')
print('\n\033[m')
print('O número {} é divisível por {} números.\n'.format(num, vezes))
if vezes == 2:
    print('É PRIMO!!!!!')
else:
    print('NÃO É PRIMO!')
