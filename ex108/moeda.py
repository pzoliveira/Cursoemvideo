def aumentar(valor, percentual):
    return moeda(valor * (1 + percentual/100))


def diminuir(valor, percentual):
    return moeda(valor * (1 - percentual/100))


def dobro(valor):
    return moeda(valor * 2)


def metade(valor):
    return moeda(valor / 2)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>4.2f}'.replace('.', ',')