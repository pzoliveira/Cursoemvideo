kmrod = float(input('Quilômetros rodados: '))
qdias = float(input('Dias: '))
valor = 0.15 * kmrod + 60 * qdias
print('Fatura: R${:.2f}'.format(valor))
