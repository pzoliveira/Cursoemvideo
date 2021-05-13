from time import sleep
def contador(i, f, p):
    if p < 0:
        p = -p
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i < f:
        for cont in range(i, f+1, p):
            print(f'{cont} ', end='')
            sleep(0.5)
    else:
        for cont in range(i, f-1, -p):
            print(f'{cont} ', end='')
            sleep(0.5)
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora escolha sua contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
