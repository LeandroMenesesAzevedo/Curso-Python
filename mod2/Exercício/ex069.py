from random import randint
v= 0
print ('='*50)
print (f'JOGO DO PAR OU IMPAR'.center(50))
print ('='*50)
while True:
    jogador = int(input('Escolha um número: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'P/p/I/i':
        tipo = str(input('PAR ou IMPAR [P/I]')).upper() .strip()[0]
        print(f' Você digitou {jogador} e o computador colocou {pc} total {total}')

        if tipo == 'P':
            print('='*50)
            if total % 2 == 0:
                print('Deu PAR.')
                print('Você VENCEUUU')
                print('='*50)
                v+=1
            else:
                print('='*50)
                print('Deu IMPAR')
                print('Você PERDEUUU')
                print('='*50)
                break
                
        elif tipo == 'I':
            print('='*50)
            if total % 2 == 1:
                print('Deu IMPAR')
                print('Você Venceu')
                print('='*50) 
                v+=1
            else: 
                print('Deu PAR.')
                print('Você PERDEUUU')
                print('='*50)
                break
                
        print ('Vamos jogar novamente ...')
    print('GAME OVER!')
