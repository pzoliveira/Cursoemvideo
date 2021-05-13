def área(largura, comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é {largura*comprimento}m2.')


# Programa Principal
print('-' * 30)
print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
larg = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))
área(larg, compr)
