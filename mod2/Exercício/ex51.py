n = int(input('Digite um número:'))
r = int(input('Digite a razão: '))

for c in range (n, 11, r):
    print ('{}'.format(c), end=' -> ' )
print ('ACABOU')