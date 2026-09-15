n = int (input(' Digite um número [Digite o número 999 para finalizar]: '))
f = 999
soma = 0
while n != f:
    n = int (input(' Digite um número [Digite o número 999 para finalizar]: '))
    print (' A quantidade de número digitado foi {} e a soma entre eles são: '.format(soma))
    soma += n
    n += 1
print('FIM')