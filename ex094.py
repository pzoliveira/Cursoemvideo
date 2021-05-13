dados = dict()
estat = list()
acumi = 0
mlhcad = list()
acmdid = list()
while True:
    dados['nome'] = str(input('Nome: ')).strip()
    dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    estat.append(dados.copy())
    escl = str(input('Quer continuar [S/N]? ')).strip()
    if escl in 'Nn':
        break
print('-=' * 25)
tam = len(estat)
print(f'A) Ao todo temos {tam} pessoas cadastradas.')
for dicio in estat:
    acumi += dicio['idade']
    if dicio['sexo'] == 'F':
        mlhcad.append(dicio['nome'])
mdidade = acumi / tam
print(f'B) A média de idade é de {mdidade} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for ind, nmmlhr in enumerate(mlhcad):
    if ind != 0:
        print(', ', end='')
    print(nmmlhr, end='')
for dicio in estat:
    if dicio['idade'] > mdidade:
        acmdid.append(dicio.copy())
print(f'\nD) Lista das pessoas que estão acima da média de idade:')
for dado in acmdid:
    print('    ', end='')
    for chave, valor in dado.items():
        print(f'{chave} = {valor}; ', end='')
    print()
