vlrtot = prodacmil = premaisb = cont = 0
while True:
    print('-=' * 18)
    nomprod = str(input('Entre com o nome do produto: '))
    preprod = float(input('Qual o valor desse produto? R$'))
    cont += 1
    vlrtot += preprod
    if preprod > 1000:
        prodacmil += 1
    if cont ==1 or preprod < premaisb:
        prodmaisb = nomprod
        premaisb = preprod
    vaicont = ' '
    while vaicont not in "SsNn":
        vaicont = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if vaicont in 'Nn':
        break
print(f'O total de compras no carrinho é R${vlrtot:.2f}')
print(f'Há {prodacmil} produtos que custam acima de R$1.000,00')
print(f'O produto {prodmaisb} é o mais barato e custa R${premaisb:.2f}')
