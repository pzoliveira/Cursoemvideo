nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média é {:.1f}'.format(media))
if media < 5.0:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO!!!')
