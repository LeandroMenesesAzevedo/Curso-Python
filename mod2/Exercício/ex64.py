n = 0
soma = 0
cont = 0
while n != 999:
    n = int (input(' Digite um número [Digite o número 999 para finalizar]: '))
    soma += n
    cont += 1
print (' A quantidade de número digitado foi {} e a soma entre eles são: {}'.format(cont, soma))