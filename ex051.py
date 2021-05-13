print('='*30)
print('DEZ PRIMEIROS TERMOS DE UMA PA')
print('='*30)
priter = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))
for termo in range(priter, priter + razao * 9 + 1, razao):
    print('{}'.format(termo), end = ' -> ')
print('ACABOU')
