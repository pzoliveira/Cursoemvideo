from ex108 import moeda

valor = float(str(input('Digite o preço: R$')).replace(',', '.'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10)}')
