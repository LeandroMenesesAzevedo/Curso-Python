from random import randint
print ('='*50)
print (f'JOGO DO PAR OU IMPAR'.center(50))
print ('='*50)
while True:
    jogador = int(input('Escolha um número: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ''
    while tipo not in 'PpIi':
        tipo = str(input('PAR ou IMPAR [P/I]')).upper() .strip()[0]
        print(f' Você digitou {jogador} e o computador colocou {pc} total {total}')

        if jogador % 2 == 0:
            print('Deu PAR.')
            print('Você VENCEUUU')
        else:
            print('Deu IMPAR')
            print('Você PERDEUUU') 
            break