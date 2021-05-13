from time import sleep
escolha = 4
while escolha != 5:
    if escolha == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        print('{}'.format(n1) if n1>n2 else '{}'.format(n2))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente!')
    print('#&' * 17)
    print('''Menu de opções:
    [1] somar os números
    [2] multipolicar os números
    [3] apresentar o maior número
    [4] entrar com novos números
    [5] sair do programa''')
    escolha = int(input('Digite a sua opção: '))
