salary = float(input('Qual é o salário do funcionário R$'))
adjustment_percentage = int(input('Qual o percentual de desconto (5, 15 ou 25)? '))

if adjustment_percentage in [5, 15, 25]:
  new_salary = salary + (salary * adjustment_percentage / 100)
  print(f'Um funcionário que ganhava R${salary:.2f}, com {adjustment_percentage}, passa a receber R${new_salary:.2f}')
else:
  print('Por favor, digite um percentual de reajuste válido. Digite 5, 15 ou 25.')

