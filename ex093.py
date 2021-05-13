desemp = dict()
golos = list()
desemp['nome'] = str(input('Nome do jogador: '))
qtde = int(input(f'Quantas partidas {desemp["nome"]} jogou? '))
for cont in range(qtde):
    golos.append(int(input(f'   Quantos gols na partida {cont}? ')))
desemp['gols'] = golos[:]
desemp['total'] = sum(golos)
print('-=' * 30)
print(desemp)
print('-=' * 30)
for chave, valor in desemp.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {desemp["nome"]} jogou {qtde} partidas.')
for ind, elem in enumerate(desemp['gols']):
    print(f'    => Na partida {ind}, fez {elem} gols.')
print(f'Foi um total de {desemp["total"]} gols.')
