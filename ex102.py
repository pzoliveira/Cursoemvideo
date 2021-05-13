def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser usado no cálculo.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do fatorial do número n.
    """
    print('-' * 30)
    result = 1
    for valor in range(n, 1, -1):
        result *= valor
        if show:
            print(f'{valor} x ', end='')
    if show:
        print('1 = ', end='')
    return result


# Programa Principal
#print(fatorial(4, True))
help(fatorial)
