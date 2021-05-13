cont = acum = 0
while True:
    num = int(input('Entre com um número inteiro (999 para parar): '))
    if num == 999:
        break
    else:
        cont += 1
        acum += num
print(f'Você digitou {cont} números cuja soma perfaz {acum}')
