sexo = str(input('Digite o sexo [ F / M ]: ')).strip().upper()[0]
while 'F' != sexo != 'M':
    sexo = str(input('\033[31mDADOS INVÁLIDOS!!!\033[m Digite novamente o sexo [ F / M ]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!!!'.format(sexo))
