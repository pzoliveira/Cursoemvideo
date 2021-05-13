from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))
idade = atual - nasc
print('Idade: {}'.format(idade))
if idade < 18:
        print('Você deve se alistar daqui a {} ano(s).'.format(18 - idade))
elif idade > 18:
    print('Você devia ter se alistado há {} ano(s) atrás!!!'.format(idade - 18))
else:
    print('Você deve se alistar imediatamente!!!!!')
