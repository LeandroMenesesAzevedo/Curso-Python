print('================ Tipos primitivos ======================')
x = input('Digite algo: ')

print('O tipo primitivo do valor é ', type(x))

print('O valor é do tipo primitivo é numerico ? {} '.format(x.isnumeric()))
print('O valor tem espaço ? {}'.format(x.isspace()))
print('O valor é do tipo esta em letras maiuscula ? {}'.format(x.isupper()))
print('O valor é do tipo esta em letras minuscula ? {}'.format(x.islower()))