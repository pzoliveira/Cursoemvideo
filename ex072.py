pextenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatoroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
escolha = -1
while escolha not in range(0, 21):
    escolha = int(input('Entre com um número entre 0 e 20: '))
    if escolha not in range(0, 21):
        print('Entrada inválida, tente novamente!', end= ' ')
print(f'Você entrou com o número {pextenso[escolha]}')
