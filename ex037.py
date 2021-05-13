numdec = int(input('Digite um número decimal inteiro: '))
print('Escolha 0 para converter para binário, 1 para octal e 2 para hexadecimal')
escolha = int(input('Digite aqui sua escolha: '))
if escolha == 0:
    print('Convertendo para binário: {}'.format(bin(numdec)[2:]))
elif escolha == 1:
    print('Convertendo para octal: {}'.format(oct(numdec)[2:]))
elif escolha == 2:
    print('Convertendo para hexadecimeal: {}'.format(hex(numdec)[2:].upper()))
else:
    print('Escolha inválida!!!')
