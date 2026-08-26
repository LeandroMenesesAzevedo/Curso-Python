print ('Gerador de PA')
print ('-=' *10)

x = int(input('Digite o valor do termo: '))
razao = int(input ('Digite a Razão da PA: '))
termo = x
cont = 1

while cont <= 10:
    print ('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
