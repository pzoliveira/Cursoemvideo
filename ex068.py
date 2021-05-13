from random import randint
cont = 0
while True:
    print('=-' * 15)
    print('JOGO DO PAR OU ÍMPAR')
    print('=-' * 15)
    aposta = int(input('Entre com sua aposta: '))
    prdd = str(input('Par ou ímpar? [P/I] ')).strip()[0]
    print('-' * 30)
    cptdr = randint(0, 11)
    soma = aposta + cptdr
    result = 'PAR' if soma % 2 == 0 else 'ÍMPAR'
    print(f'Você apostou {aposta} e o computador {cptdr}. A soma é {soma}, que é {result}')
    print('-' * 30)
    if soma % 2 == 0 and prdd in 'Pp' or soma % 2 == 1 and prdd in 'Ii':
        print('Parabéns, você acertou!')
        print('Vamos jogar mais uma vez!!!')
        cont += 1
    else:
        break
print('Você errou...')
print('=-' * 15)
print(f'FIM DE JOGO! Você acertou {cont} vezes.')
