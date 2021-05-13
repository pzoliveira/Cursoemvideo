num = int(input('Digite um número entre 1 e 9 para ver sua tabuada: '))
if 1 <= num <= 9:
    for cont in range(1, 11):
        print('{} x {:2} = {:2}'.format(num, cont, num * cont))
else:
    print('Número inválido!!!!!!')
