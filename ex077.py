palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for elem in palavras:
    print(f'A palavra {elem.upper()} contém as vogais: ', end='')
    for letra in elem:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
    print('')
