from time import sleep
from random import randint
jogo = list()
print('-' * 38)
print(f'{" SORTEIO DE JOGOS DA MEGA SENA ":#^38}')
print('-' * 38)
qtde = int(input('Para quantos jogos deseja sortear? '))
print('-=' * 7, end='')
print(f' {qtde:2} JOGOS ', end='')
print('-=' * 7)
for seq in range(qtde):
    for num in range(6):
        sinal = True
        while sinal:
            sorte = randint(1, 60)
            if len(elem) != 0:
                for elem in jogo:

        jogo.append(sorte))
    jogo.sort()
    print(f'Jogo {seq + 1}: {jogo}')
    jogo.clear()
print('-=' * 6, end='')
print(' BOA SORTE!!! ', end='')
print('-=' * 6)
