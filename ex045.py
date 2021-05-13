from random import randint
from time import sleep
print('*#*' * 9)
print('=' * 9, 'JOKENPÔ', '=' * 9)
print('*@*' * 9)
print('''\nDas opções abaixo:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
escolha = int(input('O que escolhe? '))
if 0 <= escolha <= 2:
    sleep(1)
    print('\nJO', end='')
    sleep(1)
    print('KEN', end='')
    sleep(1)
    print('PÔ')
    opcoes = ('Pedra', 'Papel', 'Tesoura')
    jogdes = opcoes[escolha]
    jogcomp = opcoes[randint(0, 2)]
    print('#' * 27)
    print('Você jogou {}'.format(jogdes.upper()))
    print('O computador jogou {}'.format(jogcomp.upper()))
    print('#' * 27)
    if jogdes == jogcomp:
        print('EMPATE')
    elif (jogdes == 'Pedra' and jogcomp == 'Tesoura') or (jogdes == 'Papel' and jogcomp == 'Pedra') or (jogdes == 'Tesoura' and jogcomp == 'Papel'):
        print('VOCÊ VENCEU!!!')
    else:
        print('COMPUTADOR GANHOU! HE HE HE')
else:
    print('ESCOLHA INVÁLIDA')
