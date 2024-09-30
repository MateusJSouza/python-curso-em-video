import math

angle = float(input('Digite o ângulo que você deseja: '))

# Convertendo graus para radianos
radians = math.radians(angle)

# Cálculo do seno, cosseno e tangente
sine = math.sin(radians)
cosine = math.cos(radians)
tangent = math.tan(radians)

print(f'O ângulo de {angle}° tem o SENO de: {sine:.2f}')
print(f'O ângulo de {angle}° tem o COSSENO de: {cosine:.2f}')
print(f'O ângulo de {angle}° tem a TANGENTE de: {tangent:.2f}')