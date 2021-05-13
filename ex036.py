casa = float(input("Entre com o valor da casa: R$"))
salario = float(input('Qual o seu salário? R$'))
qtanos = int(input('Em quantos anos pretende pagar o empréstimo? '))
prestacao = casa / 12 / qtanos
if prestacao > salario * 0.30:
    print('Empréstimo NEGADO, salário insuficiente para pagar prestação de R${:.2f}!'.format(prestacao))
else:
    print('Empréstimo CONCEDIDO, valor da prestação de R${:.2f}'.format(prestacao))
