def ficha(jogador='<desconhecido>', numgols=0):
    return f'O jogador {jogador} fez {numgols} gols no campeonato.'


# Programa Prinicipal
print('-' * 30)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: ')).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome != '':
    print(ficha(nome, gols))
else:
    print(ficha(numgols=gols))
