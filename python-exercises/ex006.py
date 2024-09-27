import math

n = int(input('Digite um número: '))

double = n * 2
triple = n  * 3
square_root = math.sqrt(n)

print(f'O dobro de {n} vale {double}')
print(f'O triplo de {n} vale {triple}')
print(f'A raiz quadrada de {n} é {square_root:.2f}.')