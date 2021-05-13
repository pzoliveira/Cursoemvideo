peso = float(input('Quel é o seu peso (kg)? '))
altura = float(input('Qual é a sua altura(m)? '))
imc = peso / (altura ** 2)
print('IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
