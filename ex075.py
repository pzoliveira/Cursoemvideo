numtupla = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
            int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))
print(f'Você digitou os seguintes números: {numtupla}')
if 9 in numtupla:
    print(f'Foram digitados {numtupla.count(9)} números 9')
if 3 in numtupla:
    print(f'Foi digitado o primeiro número 3 na {numtupla.index(3) + 1}ª posição')
print('Foram digitados os seguintes números pares: ', end='')
for elemento in numtupla:
    if elemento % 2 == 0:
        print(f'{elemento}', end=' ')
