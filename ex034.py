salario = float(input('\nDigite o salário: R$'))
percentual = 1.15 if salario <=1250 else 1.1
print('\nNovo salário: R${:.2f}'.format(salario * percentual))
