full_name = str(input('Digite seu nome completo: '))

# Contagem do total de letras do nome completo
total_words = len(full_name.replace(' ', ''))

# Contagem de letras do primeiro nome
first_name = full_name.split()[0]
letter_first_name = len(first_name)

print(f'Seu nome em maiúsculas é {full_name.upper()}')
print(f'Seu nome em minúsculas é {full_name.lower()}')
print(f'Seu nome tem ao todo {total_words} letras')
print(f'Seu primeiro nome possui um total de {letter_first_name} letras')