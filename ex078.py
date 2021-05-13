valores = list()
for pos in range(5):
    valores.append(int(input(f'Digite um valor para a posição {pos}: ')))
print('$' * 40)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições:', end=' ')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições:', end=' ')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
