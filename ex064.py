acum = cont = num = 0
while num != 999:
    num = int(input('Entre com um número inteiro [999 -> parada]: '))
    acum += num if num != 999 else 0
    cont += 1 if num != 999 else 0
print('Foram digitados {} números, cuja soma resulta em {}'.format(cont, acum))
