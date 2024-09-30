daily_rate = 60 # Valor por dia
km_rate = 0.15 # Valor por km rodado

days_rented = int(input('Quantos dias alugados? '))
km_driven = float(input('Quantos Km rodados? '))

# Cálculo do total
total = (days_rented * daily_rate) + (km_driven * km_rate)

print(f'O total a pagar é R${total:.2f}')