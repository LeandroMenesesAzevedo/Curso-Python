salario =float(input(' Digite o salário do funcionário R$: '))

if salario > 1250:
    novo_salario = salario + (salario * 10/100) 
if salario <= 1250:
    novo_salario = salario + (salario * 15/100)

print ('Quem ganhava R${} recebeu um aumento e o novo salário é R${}'.format(salario, novo_salario))
    
