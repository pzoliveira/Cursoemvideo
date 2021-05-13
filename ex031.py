dist = float(input('Distância da viagem: '))
valor = dist * 0.5 if dist <= 200 else dist * 0.45
print('O preço da passagem é R${:.2f}'.format(valor))
