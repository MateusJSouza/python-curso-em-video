msg = input('Digite algo: ')

data_type = type(msg) # tipo primitivo
has_spaces = msg.isspace() # se possui espaços
is_number = msg.isdigit() # se é um número
is_alphabetic = msg.isalpha() # se é alfabético
is_uppercase = msg.isupper() # se está em maiúsculas
is_lowercase = msg.islower() # se está em minúsculas
is_capitalized = msg.istitle() # se está capitalizada

print(f'O tipo primitivo deste valor é {data_type}')
print(f'Só tem espaços? {has_spaces}')
print(f'É um número? {is_number}')
print(f'É alfabético? {is_alphabetic}')
print(f'É maiúsculas? {is_uppercase}')
print(f'É minúsculas? {is_lowercase}')
print(f'É capitalizada? {is_capitalized}')