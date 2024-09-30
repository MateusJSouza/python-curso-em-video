from math import hypot

opposite = float(input('Comprimento do cateto oposto: '))
adjacent = float(input('Comprimento do cateto adjacente: '))

# Usando hypot do pacote math
hypotenuse = hypot(opposite, adjacent)

# Usando math para calcular a raiz quadrada
# hypotenuse = math.sqrt(opposite ** 2 + adjacent ** 2)

# Usando a função pow()
# hypotenuse = math.sqrt(pow(opposite, 2) + pow(adjacent, 2))

print('A hipotenusa vai medir {:.2f}'.format(hypotenuse))