from random import randint
from time import sleep
from operator import itemgetter
halea = list()
jogr = dict()
print('Os lances dos dados por jogador:')
for cont in range(4):
    lance = randint(1, 6)
    jogr[f'jogador{cont + 1}'] = lance
    print(f'O jogador {cont + 1} tirou {lance} no dado.')
    sleep(1)
print('-=' * 20)
print('  == RANKING DOS JOGADORES ==')
halea = sorted(jogr.items(), key=itemgetter(1), reverse=True)
for ind, dado in enumerate(halea):
    print(f'   {ind + 1}o. lugar: {dado[0]} com {dado[1]}')
    sleep(1)
