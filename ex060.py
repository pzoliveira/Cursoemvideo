num = int(input('Digite um número para calcular seu fatorial: '))
result = ''
calcnum = 1
for c in range(num, 0, -1):
    result = result + str(c) + ' x '
    calcnum *= c
calctext = result[:len(result)-3]
print('{}! = {} = {}'.format(num, calctext, calcnum))
