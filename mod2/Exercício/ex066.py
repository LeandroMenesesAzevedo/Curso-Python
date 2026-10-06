resp = 'S'
soma = quantidade = media = maior = menor =  0
while resp in 'Ss':
    num = int( input (' Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor= num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num


    #colocamos tudo que usuário digita em letra maiuscula, sem espaço e considerando só a primeira letra.
    resp = str(input('Deseja continuar [s/n]')).upper() .strip()[0]
media = soma/quantidade
print ('O maior número foi {} e o menor número {}'.format(maior, menor))
print ('A Quantidade de números foram {} e a  media dos valores são {}' .format(quantidade, media))
