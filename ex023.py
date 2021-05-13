num = int(str(input('Digite um número: ')).strip())
milhar = num // 1000
centena = (num - milhar * 1000) // 100
dezena = (num -(milhar * 1000 + centena * 100)) // 10
unidade = num % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))