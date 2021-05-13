acum = 0
for cont in range(0, 6):
    num = int(input('\nDigite um número inteiro: '))
    acum += num if num % 2 == 0 else 0
print('\nA soma de todos os números pares: {}'.format(acum))
