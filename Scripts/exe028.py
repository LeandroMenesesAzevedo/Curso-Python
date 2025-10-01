from random import randint
computador = randint(0 , 5) # FAZ O COMPUTADOR SORTEAR UM NÚMERO DE 0 A 5
print('*' * 20)
num = int(input('Tente adivinhar um número que estou pensando: '))
print('*' * 20)
print ('PROCESSANDO ...')
if num == computador:
    print('PARABÉNS VOCÊ ACERTOU! ')
    print(' O número que estou pensando é {}'.format(num))
else:
    print('VOCÊ PERDEU')
    print ('O número que estou pensando é {} e não {}.'.format(computador, num))


