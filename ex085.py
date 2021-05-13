listanum = [[], []]
for cont in range(7):
    num = int(input(f'Digite o {cont + 1}o. número: '))
    if num % 2 == 0:
        listanum[0].append(num)
    else:
        listanum[1].append(num)
listanum[0].sort()
listanum[1].sort()
print('-=' * 30)
print(f'A lista de números pares é {listanum[0]}')
print(f'A lista de números ímpares é {listanum[1]}')
