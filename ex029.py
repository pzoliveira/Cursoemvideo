velat = int(input('Qual a velocidade atual? '))
if velat > 80:
    print('Você foi multado, velocidade limite de 80km/h!!!')
    print('Pagar multa de R${},00'.format((velat - 80)*7))
print('Tenha um bom dia! Dirija com segurança!')
