print('========== Preço da viagem ==========')
distancia = int(input(' Qual a distância percorrida em km da viagem?  '))
if distancia <= 200:
    valor =  distancia * 0.50
    print (' O valor percorrido foi {} KM'.format(distancia))
    print (' O valor da viagem é R$ {:.2f}'.format(valor))
else:
    valor  = distancia * 0.45
    print (' O valor percorrido foi{} KM'.format(distancia))
    print (' O valor da viagem é R$ {:.2f}'.format(valor))

print('==========  Tenha uma boa Viagem ===========')


