from datetime import date
vano = int(input('Digite o ano ou 0 para o ano atual: '))
if vano == 0:
    vano = date.today().year
if vano % 4 == 0 and vano % 100 != 0 or vano % 400 == 0:
    print('O ano {} é bissexto.'.format(vano))
else:
    print('O ano {} não é bissexto.'.format(vano))
