from random import randrange
numaleat = (randrange(11), randrange(11), randrange(11), randrange(11), randrange(11))
print('-=' * 37)
print('Foram sorteados os seguintes cinco números aleatoriamente:', end=' ')
for seq in numaleat:
    print(seq, end=' ')
print('')
print('-=' * 37)
print(f'O maior número sorteado foi {max(numaleat)}')
print(f'O menor número sorteado foi {min(numaleat)}')
