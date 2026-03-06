from random import randint
from time import sleep

itens =('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''
    [1] - Pedra
    [2] - Papel
    [3] - Tesoura
''')
op = int(input(' Escolha uma opção: '))

if op == 1:
        if computador == 1:
            print ('Você escolheu a opção {}'.format(op))
            print (' O computador escolheu {}'.format(itens[computador]))
            print ('DEU EMPATE')
        elif computador == 2:
            print ('Você escolheu a opção {}'.format(op))
            print (' O computador escolheu {}'.format(itens[computador]))
            print ('Você venceu')
        elif computador == 3:
            print('Você escolheu a opção {}'.format(op))
            print ('O computador escolheu  {}'.format(itens[computador]))
            print ( 'O computado venceu!!!')

elif computador == 2:
        print('teste')
elif computador == 3:
        print('teste')