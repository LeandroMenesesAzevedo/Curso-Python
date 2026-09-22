print('*' *20)
print(' TABUADA ')
print('*'*20)
n = int (input('Digite um número: '))

cont = 1
num = 1
c = ''
while c == 'S/s':
    while cont <= 10:
            print ('{} X {} = {}'.format(n, num, n*num))
            num += 1
            cont += 1
    c = input ('Deseja continuar[S/N] = ')