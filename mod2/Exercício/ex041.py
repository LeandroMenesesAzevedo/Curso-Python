print( 'Condição de existencia de um triângulo')

la = int(input( 'Digite o valor do primeiro lado: '))
lb = int(input( 'Digite o valor do segundo lado: '))
lc = int(input( 'Digite o valor do terceiro lado: '))

if la < lb + lc and lb < la + lc and lc < la + lb:
    print ('Esses segmentos formam um triângulo')

    if la == lb == lc:
        print ('Esse é um triângulo equilátero')
    elif la != lb != lc !=la:
        print ('Esse é um triângulo escaleno')
    else: 
        print ('Esse é um triângulo isóceles')
else:
    print (' Esses segmentos não formam triângulo')