from datetime import date
maior = menor = 0
for num in range(1, 8):
    anonasc = int(input('Em qua ano nasceu a {}a. pessoa? '.format(num)))
    if date.today().year - anonasc > 20:
        maior += 1
    else:
        menor += 1
print('A quantidade de pessoas maiores de idade é {} e de menores de idade é {}'.format(maior, menor))
