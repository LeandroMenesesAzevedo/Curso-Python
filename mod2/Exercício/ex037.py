print ('********************** CONVERSOR DE NÚMERO **************************')
num = (int(input('\n'' Digite um número: ')))

print (' Escolha uma opção abaixo: \n')
print (' 1 - Conversor Binário ')
print (' 2 - Conversor Octal')
print (' 3 - Conversor Hexadecimal')

op = (int (input('\n''Qual opção acima deseja que o seu número seja convertido: ')))
if op== 1:
    nb = bin(num)
    print(' O número digitado foi {}' .format(num))
    print(' O valor  em binário é: \033[32m{}\33[0m'.format(nb))
elif op == 2:
    numo = oct(num)
    print ('O número digitado foi {}'.format (num))
    print ('O valor em octal é : \033[32m{}\033[0m'.format(numo))
elif op == 3:
    numh = hex(num)
    print (' O número digitado foi {}'.format (num))
    print (' O valor em hexadecimal é: \033[32m{}\033[0m'.format(numh))
else:
    print('\033[31m OPÇÃO INVALÍDA\033[0m')