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

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if op == 1:
        if computador == 0:
            print ('Você escolheu a opção {}'.format(op))
            print (' O computador escolheu {}'.format(itens[computador]))
            print ('DEU EMPATE')
        elif computador == 1:
            print ('Você escolheu a opção {}'.format(op))
            print (' O computador escolheu {}'.format(itens[computador]))
            print ('Você perdeu')
        elif computador == 2:
            print('Você escolheu a opção {}'.format(op))
            print ('O computador escolheu  {}'.format(itens[computador]))
            print ( 'Você venceu!!!')

elif op == 2:
        if computador == 0:
              print ('Você escolheu a opção {}'.format(op))
              print ('O computador escolheu {}'.format(itens[computador]))
              print ('VOCÊ VENCEU')
        elif computador == 1:
            print ('Você escolheu a opção {}'.format(op))
            print ('O computador escolheu {}'.format(itens[computador]))
            print ('DEU EMPATE')
        elif computador == 2:
            print ('Você escolheu a opção {}'.format(op))
            print ('O computador escolheu {}'.format (itens[computador]))
            print('VOCÊ PERDEU')             
elif op == 3:
        if computador == 0:
              print('Você escolheu a opção {}'.format(op))
              print('O computador escolheu {}'.format(itens[computador]))
              print('VOCÊ PERDEU')
        elif computador == 1:
              print('Você escolheu a opção {}'.format(op))
              print('O computador escolheu {}'.format(itens[computador]))
              print('VOCÊ VENCEU')
        elif computador == 2:
              print('Você escolheu a opção {}'.format(op))
              print('O computador escolheu {}'.format(itens[computador]))
              print('DEU EMPATE')