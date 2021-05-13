matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
acumpar = acum3c = maior2l = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)
for lin, lint in enumerate(matriz):
    print('[', end='')
    for col, elem in enumerate(lint):
        print(f'{elem:^5}', end='')
        if elem % 2 == 0:
            acumpar += elem
        if col == 2:
            acum3c += elem
        if lin == 1:
            if col == 0 or maior2l < elem:
                maior2l = elem
    print(']')
print('-=' * 30)
print(f'A soma dos valores pares é {acumpar}')
print(f'A soma dos valores da terceira coluna é {acum3c}')
print(f'O maior valor da segunda linha é {maior2l}')
