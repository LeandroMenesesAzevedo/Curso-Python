from math import floor # importamos na biblioteca math a função floor para arredondar o número para valor menor.

num = float (input( 'Digite um número: ' ))
sub = floor(num) # arredondando o número para menor

print( 'O número digitado foi {} e o resultado arredondando para menor{}'.format(num, sub) )
