desemp = dict()
golos = list()
dados = []
while True:
    desemp['nome'] = str(input('Nome do jogador: '))
    qtde = int(input(f'Quantas partidas {desemp["nome"]} jogou? '))
    for cont in range(qtde):
        golos.append(int(input(f'   Quantos gols na partida {cont + 1}? ')))
    desemp['gols'] = golos[:]
    desemp['total'] = sum(golos)
    dados.append(desemp.copy())
    golos.clear()
    escolha = str(input('Deseja continuar [S/N]? ')).strip()[0]
    if escolha in 'Nn':
        break
print('-=' * 30)
print('cod  nome        gols            total')
print('-' * 39)
for ind, val in enumerate(dados):
    print(f'{ind:>3}  {val["nome"]:<12}{str(val["gols"]):<16}{val["total"]:<12}')
while True:
    print('-' * 39)
    mostra = int(input('Mostrar dados de qual jogador (999 interrompe)? '))
    if mostra == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {dados[mostra]["nome"]}:')
    for ind, elem in enumerate(dados[mostra]['gols']):
        print(f'    => Na partida {ind + 1}, fez {elem} gols.')
print('<<< VOLTE SEMPRE!!! >>>')
