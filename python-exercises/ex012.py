price = float(input('Qual é o preço do produto? R$'))
discount_percentage = int(input('Qual o percentual de desconto (5, 15 ou 25)? '))

if discount_percentage in [5, 15, 25]:
  discount = price - (price * discount_percentage / 100)
  print(f'O produto que custava R${price:.2f}, na promoção com desconto de {discount_percentage}% vai custar R${discount:.2f}')
else:
  print('Desconto inválido. Por favor, digite 5, 15 ou 25.')

