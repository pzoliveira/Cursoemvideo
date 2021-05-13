acum = 0
cont = 0
for num in range(3, 501, 6):
    acum += num
    cont += 1
print('{} números ímpares múltiplos de 3 no intervalo de 1 a 500 aprseentam a soma de {}'.format(cont, acum))
