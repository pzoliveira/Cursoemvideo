matriz = [[], [], []]
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Entre com um valor para [{linha},{coluna}]: '))
        matriz[linha].append(valor)
print('-=' * 30)
for lint in matriz:
    print('[', end='')
    for elem in lint:
        print(f'{elem:^5}', end='')
    print(']')
