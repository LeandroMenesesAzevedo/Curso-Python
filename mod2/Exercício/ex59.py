import time
n1 = int (input('Digite um valor: '))
n2 = int (input('Digite outro valor:  '))
op = '0'

while op != 5:
    print('=' * 50)
    print('''        [1] Somar 
        [2] Subtrair
        [3] Multiplicar
        [4] Divisão
        [5] Finalizar o programa
        ''')
    print ('=' * 50)
    op = int(input ('Escolha uma opção: '))

    if op == 1:
        soma = n1 +n2
        print('...')
        time.sleep(1)
        print ('{} + {} = {}'.format(n1, n2 , soma))
        print ('_' * 50)
        time.sleep(2)
        op = int(input ('Escolha uma opção: ')) 

    elif op == 2:
        sub = n1 - n2
        print('...')
        time.sleep(1)
        print ('{} - {} = {}'.format(n1, n2, sub))
        print('_ '*50)
        time.sleep(2)
        op = int(input('Escolha uma opção: '))

    elif op == 3:
        mult = n1 * n2
        print('...')
        time.sleep(1)
        print('{} * {} = {}'.format(n1, n2, mult))
        print ('_' *50)
        time.sleep(2)
        op = int(input('Escolha uma opção: '))

    elif op == 4:
        divisao = n1/n2
        print('...')
        time.sleep(1)
        print('{} / {} = {}'.format(n1, n2, divisao))
        print('_' * 50)
        time.sleep(2)
        op=(int(input('Escolha uma opção: ')))
    
    else :
        print('...')
        time.sleep(1)
        print('Opção inválida')
        print('_' * 50)
        time.sleep(0.5)



print('...')
time.sleep (1)
print('PROGRAMA FINALIZADO')

