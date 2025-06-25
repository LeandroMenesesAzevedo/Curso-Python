print('============ Salário =================')

n = float(input(' Digite o salário atual do funcionário: '))

salf = n + ( n * 0.15 )

print('O salário com reajuste de 15% é: R${:.2f}'.format(salf))
