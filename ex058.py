from random import randint
numaleat = randint(0, 10)
numpal = 0
numesc = -1
while numesc != numaleat:
    numesc = int(input('Tente adivinhar um número entre 0 e 10 que o computador sorteou: '))
    numpal += 1
    if numesc < numaleat:
        print('Mais... Tente de novo!!!')
    elif numesc > numaleat:
        print('Menos... Tente de novo!!!')
print('\033[33mVOCÊ ACERTOU!!!!!\033[m')
print('Número de tentativas: {}'.format(numpal))
