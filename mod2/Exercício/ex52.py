tt =  0
n = int (input('Digite um número: '))

for c in range (1, 11):
    if n % c == 0:
        print('\033[32m', end=' ')
        tt += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print ('\n \033[m O número digitado foi {} e foi dividido {} vezes'.format(n, tt))
if tt == 2:
    print (' O NÚMERO É PRIMO')
else:
    print(' O NÚMERO NÃO É PRIMO')

