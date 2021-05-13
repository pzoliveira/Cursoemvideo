def leiaInt(texto):
    """
    -> Lê a partir do teclado um número que deve ser inteiro
    :param texto: Mensagem de entrada de dados.
    :return: O valor do número inteiro.
    """
    print('-' * 30)
    while True:
        núm = str(input(texto)).strip()
        if núm.isnumeric():
            return int(núm)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número inteiro {n}')
