prodpre = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
           'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas',
           22.30, 'Livro', 34.90)
print('-=' * 20)
print(f'{"MATERIAIS ESCOLARES":^40}')
print('-=' * 20)
for ind, elem in enumerate(prodpre):
    if ind % 2 == 0:
        print(f'{elem:.<31}', end='R$ ')
    else:
        print(f'{elem:>6.2f}')
print('-=' * 20)
