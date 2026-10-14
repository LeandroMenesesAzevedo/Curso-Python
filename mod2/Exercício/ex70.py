print('='*50)
print(f'CASTRADO DE CLIENTE'.center(50))
print('='*50)

resp = 'S'
while resp in 'S/s':
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))
    resp = str(input('Deseja continuar [S/N]: ')).upper() .strip()[0]
    