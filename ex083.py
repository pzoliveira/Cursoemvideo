expressao = input('Entre com uma expressão matemática: ')
contparent = 0
for elem in expressao:
    if elem == '(':
        contparent += 1
    elif elem == ')':
        contparent -= 1
        if contparent < 0:
            break
if contparent == 0:
    print('Expressão correta!!!!!')
else:
    print('Expressão com erro!!!')
