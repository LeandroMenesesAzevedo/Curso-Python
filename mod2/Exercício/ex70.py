maior = masc = fem = 0
resp = 'S'
print('='*50)
print(f'CASTRADO DE CLIENTE'.center(50))
print('='*50)

while True:
    while resp in 'S/s':
        idade = int(input('Digite a idade: '))
        sexo = str(input('Digite o sexo [M/F]: '))
        if idade >= 18:
            maior += 1 
        else:
            print('CADASTRO NÃO REALIZADO MENOR DE 18 ANOS')
            break
        resp = str(input('Deseja continuar [S/N]: ')).upper() .strip()[0]
        
        if sexo in 'M/m':
            masc += 1
        else:
            fem += 1

print (f'A quantidade de pessoas maior de 18 anos são: {maior}')
print (f'A quantidade de homens cadastrados são: {masc}')
print (f'A quantidade de mulheres cadastradas são: {fem}')