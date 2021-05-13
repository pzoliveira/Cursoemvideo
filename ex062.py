print('Criador de PA com termos adicionais')
print('-=' * 20)
priter = int(input('Entre o primeiro termo da PA: '))
razao = int(input('Entre a razão da PA: '))
cont = 0
print('Os dez primeiros termos dessa PA são:')
termon = priter
qtdetermos = 10
termosad = 10
while termosad > 0:
    while cont < qtdetermos:
        print('{} ¬ '.format(termon), end='')
        termon += razao
        cont += 1
    print('PAUSA')
    termosad = int(input('Quantos termos adicionais você deseja? '))
    qtdetermos += termosad
print('-=' * 20)
print('Foram mostrados {} termos dessa PA.'.format(qtdetermos))
