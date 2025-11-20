from math import hypot # importamos a função de calcular a hipotenusa da bibliteca math

co = float ( input ( 'Digite o valor do cateto oposto: ' ) )
ca = float ( input ( 'Digite o valor do cateto adjacente: ' ) )

hi = hypot(co, ca) # ultilizamos a função com os valores  do cateto aposto e cateto adjacente digitado.

print( 'O valor da hipotenusa é: {:.2f}'.format( hi ) )
