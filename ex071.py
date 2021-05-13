print('-=' * 15)
print('{:^30}'.format('BANCO PYTHON'))
print('-=' * 15)
valor = int(input('Valor a ser sacado: R$'))
onca = int(valor / 50)
macaco = int((valor - onca * 50) / 20)
arara = int((valor - onca * 50 - macaco * 20) / 10)
cara = valor - onca * 50 - macaco * 20 - arara * 10
print(f'Seu saque de R${valor:2.2f} foi realizado com sucesso!!!')
print('Quantidade de cédulas:')
if onca != 0:
    print(f'{onca:2.0f} notas de R$50.00')
if macaco !=0:
    print(f'{macaco:2.0f} notas de R$20.00')
if arara !=0:
    print(f'{arara:2.0f} notas de R$10.00')
if cara !=0:
    print(f'{cara:2.0f} notas de R$1.00')
