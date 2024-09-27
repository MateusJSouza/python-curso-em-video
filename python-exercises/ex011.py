width_wall = float(input('Largura da parede: '))
height_wall = float(input('Altura da parede: '))

# Cálculo da área
area = width_wall * height_wall

# Cálculo da quantidade de tinta necessária
liters_needed = area / 2 # 1 litro cobre 2 m²

print(f'Sua parede tem a dimensão de {width_wall}x{height_wall} e sua área é de {area}m².')
print(f'Para pintar a parede, você precisará de {liters_needed}l de tinta.')