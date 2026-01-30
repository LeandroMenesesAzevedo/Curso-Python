print( 'Condição de existencia de um triângulo')

la = int(input( 'Digite o valor do primeiro lado: '))
lb = int(input( 'Digite o valor do segundo lado: '))
lc = int(input( 'Digite o valor do terceiro lado: '))

soma = lb + lc # realizado a soma de dois lados para comparar

if (la < soma ):
    print ('não forma um triângulo')
elif (la > soma):
    print (' É um triângulo')