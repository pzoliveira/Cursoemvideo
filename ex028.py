from random import randint
ncomp = randint(0, 5)
tent = int(input('Número: '))
'''/*print('Acertou!!!' if tent == ncomp else 'Errou, pensei em {}'.format(ncomp))'''
if tent == ncomp:
    print('Acertou!!!')
else:
    print('Errou, pensei em {}'.format(ncomp))
