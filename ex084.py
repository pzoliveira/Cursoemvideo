pessoapeso = tuple()
analisedados = list()
listapesadas = list()
listaleves = list()
menor = maior = 0
while True:
    pessoapeso = [str(input('Nome: ')), float(input('Peso: '))]
    analisedados.append(pessoapeso[:])
    escolha = str(input('Deseja continuar? [s/n] ')).strip()
    if escolha == 'n':
        break
for indice, elemento in enumerate(analisedados):
    if indice == 0:
        menor = maior = elemento[1]
    else:
        if menor > elemento[1]:
            menor = elemento[1]
        if maior < elemento[1]:
            maior = elemento[1]
print(f'Foram cadastradas {len(analisedados)} pessoas.')
print('As pessoas mais pesadas são: ', end='')
for elemento in analisedados:
    if elemento[1] == maior:
        listapesadas.append(elemento[0])
print(listapesadas)
print('As pessoas mais leves são: ', end='')
for elemento in analisedados:
    if elemento[1] == menor:
        listaleves.append(elemento[0])
print(listaleves)
