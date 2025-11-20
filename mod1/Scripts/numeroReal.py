from math import trunc # importamos dentro da biblioteca  math a função trunc que retorna a parte inteira do número

num = float( input (' Digite um número: '))
print ('O valor digitado foi {} e o valor inteiro é: {}'.format(num, trunc(num)))
