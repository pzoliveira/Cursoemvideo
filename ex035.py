prise = float(input('Primeiro segmento: '))
sese = float(input('Segundo segmento: '))
terse = float(input('Terceiro segmento: '))
maior = prise
if sese > prise and sese > terse:
    maior = sese
if terse > prise and terse > sese:
    maior = terse
print('Formam triângulo!!!' if maior < (prise + sese + terse - maior) else 'NÃO formam triângulo...')
