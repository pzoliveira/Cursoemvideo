from datetime import date
anasc = int(input('Informe o ano de nascimento da atleta: '))
aatual = date.today().year
idade = aatual - anasc
print('A atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JÚNIOR.')
elif idade <= 25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
