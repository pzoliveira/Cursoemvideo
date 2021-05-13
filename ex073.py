
brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético Mineiro', 'Atlético Paranaense',
               'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco da Gama',
               'Sport', 'América Mineiro', 'Vitória', 'Paraná')
print('A tabela do campeonato brasileiro por ordem de colocação é apresentada a seguir:')
print(f'{brasileirao}')
print(f'Os cinco primeiros colocados são: {brasileirao[:5]}')
print(f'Os últimos quatro colocados são: {brasileirao[-4:]}')
chapeco = brasileirao.index('Chapecoense') + 1
ordenado = sorted(brasileirao)
print('Os times em ordem alfabética são apresentados a seguir:')
print(f'{ordenado}')
print(f'O time Chapecoense está na {chapeco}ª posição.')
