def vota(anonasc):
    from datetime import date
    idade = date.today().year - anonasc
    print(end='')
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal
print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(vota(ano))
