from math import sin, cos, tan, radians

angle = float(input('Digite o ângulo que você deseja: '))

# Convertendo graus para radianos
radians = radians(angle)

# Cálculo do seno, cosseno e tangente
sine = sin(radians)
cosine = cos(radians)
tangent = tan(radians)

print(f'O ângulo de {angle}° tem o SENO de: {sine:.2f}')
print(f'O ângulo de {angle}° tem o COSSENO de: {cosine:.2f}')
print(f'O ângulo de {angle}° tem a TANGENTE de: {tangent:.2f}')