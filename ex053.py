frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('A frase digitada sem espaços e em maiúsculas foi {} e na ordem inversa é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos aqui um caso de PALÍNDROMO!!!!')
else:
    print('Não forma palíndromo...')
