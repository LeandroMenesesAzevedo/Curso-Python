print ('Gerador de PA')
print ('*' *20)

num = int(input(' DIGITE O VALOR DO TERMO -> '))
razao = int(input('DIGITE O VALOR DA RAZAO -> '))
termo = num
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print ('{} ->'.format(termo), end = '')
        termo += razao
        cont += 1
    print( ' PAUSA ')
    mais = int (input('Quantos termos você deseja apresentar: '))
print ('A quantidade de progressões foi {}'.format(total))