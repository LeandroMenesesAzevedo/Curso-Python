print('*' *20)
print(' TABUADA ')
print('*'*20)
n = int (input('Digite um número: '))

cont = 1
num = 1
while cont <= 10:
        print ('{} X {} = {}'.format(n, num, n*num))
        num += 1
        cont += 1
