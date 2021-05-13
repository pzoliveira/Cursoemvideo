print('Criador de PA')
print('-=' * 10)
priter = float(input('Entre o primeiro termo da PA: '))
razao = float(input('Entre a razão da PA: '))
cont = 0
print('Os dez primeiros termos dessa PA são:')
while cont < 10:
    termon = priter + razao * cont
    print('{} ¬ '.format(termon), end='')
    cont += 1
print('FIM')
