print('+' * 22)
print('Seqüência de Fibonacci')
print('+' * 22)
ntermos = int(input('Quantos termos dessa seqüência você deseja ver? '))
ntermos -= 2
FNm2 = 0
FNm1 = 1
cont = 0
print('{} ¬ {} ¬ '.format(FNm2, FNm1), end='')
while cont < ntermos:
    FN = FNm1 + FNm2
    FNm2 = FNm1
    FNm1 = FN
    cont += 1
    print('{} ¬ '.format(FN), end='')
print('FIM')
