maior =0
resp = 'S'
print('='*50)
print(f'CASTRADO DE CLIENTE'.center(50))
print('='*50)
while resp in 'S/s':
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: '))
    resp = str(input('Deseja continuar [S/N]: ')).upper() .strip()[0]

    if idade > 18:
        maior +=1 

print (f'A quantidade de pessoas maior de 18 anos são: {maior}')
