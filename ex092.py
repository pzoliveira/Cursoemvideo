from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (o não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + dados['contratação'] + 35 - datetime.now().year
print('-=' * 20)
for chave, valor in dados.items():
    print(f'  - {chave} tem o valor {valor}')
