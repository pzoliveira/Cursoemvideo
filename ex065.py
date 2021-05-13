escolha = 's'
contnum = somanum = 0
maiornum = -25000
menornum = 25000
while escolha in 'sS':
    num = int(input('Entre com um número inteiro: '))
    if num > maiornum:
        maiornum = num
    if num < menornum:
        menornum = num
    contnum += 1
    somanum += num
    escolha = str(input('Deseja continuar [S/N]? ')).strip()[0]
medianum = somanum / contnum
print(f'Você entrou com {contnum} números inteiros.')
print(f'A média desses números é {medianum:.2f}.')
print(f'O maior valor digitado foi {maiornum} e o menor, {menornum}.')
