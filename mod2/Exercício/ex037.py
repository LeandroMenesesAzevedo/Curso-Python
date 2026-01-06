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
    #/ colocamos o [2: ] para tirar as duas primeiras casa  
    print(' O valor  em binário é: \033[32m{}\33[0m'.format(nb [2: ]))
elif op == 2:
    numo = oct(num)
    print ('O número digitado foi {}'.format (num))
    #/ colocamos o [2: ] para tirar as duas primeiras casa  
    print ('O valor em octal é : \033[32m{}\033[0m'.format(num[2:]))
elif op == 3:
    numh = hex(num)
    print (' O número digitado foi {}'.format (num))
    #/ colocamos o [2: ] para tirar as duas primeiras casa  
    print (' O valor em hexadecimal é: \033[32m{}\033[0m'.format(numh [2:]))
else:
    print('\033[31m OPÇÃO INVALÍDA\033[0m')