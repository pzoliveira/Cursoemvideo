print('{:=^40}'.format(' LOJAS ZAPATA '))
valor = float(input('Valor das compras: R$'))
print('''\nFORMAS DE PAGAMENTO
[ 0 ] à vista no dinheiro ou no cartão
[ 1 ] à vista no cartão
[ 2 ] em 2x vezes no cartão
[ 3 ] em 3x ou mais no cartão''')
escolha = int(input('Qual é a opção? '))
if escolha == 0:
    total = valor * 0.90
elif escolha == 1:
    total = valor * 0.95
elif escolha == 2:
    total = valor
    print('\nA compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(total / 2))
elif escolha == 3:
    total = valor * 1.20
    vezes = int(input('\nEm quantas vezss? '))
    print(('\nA compra será parcelada em {}x de R${:.2f} COM JUROS'.format(vezes, total / vezes)))
else:
    print('\nOPÇÃO INVÁLIDA!!!!')
    total = valor
print('\nAo final do pagamento, o valor total das compras será de R${:.2f}'.format(total))
