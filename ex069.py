print('-' * 24)
print('CADASTRAMENTO DE PESSOAS')
print('-' * 24)
homem = maior18 = mulhermenor20 = 0
while True:
    idade = int(input('Digite a idade da pessoa (em anos): '))
    sexo = str(input('Qual o sexo dessa pessoa [M/F]? ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1
    print('$' * 44)
    pergunta = str(input('Deseja continuar com o cadastramento {S/N]? ')).strip()[0]
    print('-' * 24)
    if pergunta in 'nN':
        break
print(f'Há {maior18} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Há {mulhermenor20} mulheres com menos de 20 anos.')
