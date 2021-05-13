while True:
    valor = int(input('Quer a tabuada de qual número? '))
    if valor >= 0:
        print('-' * 35)
        for cont in range(1, 11):
            print(f'{valor} x {cont} = {valor * cont}')
        print('-' * 35)
    else:
        break
print('FIM DO PROGRAMA!')
