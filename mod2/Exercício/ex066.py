resp = 'S'
soma = quantidade = media = maior = menor =  0
while resp in 'Ss':
    num = int( input (' Digite um número: '))
    soma += num
    quantidade += 1
    if maior == menor == 1:
        maior = num

    #colocamos tudo que usuário digita em letra maiuscula, sem espaço e considerando só a primeira letra.
    resp = str(input('Deseja continuar [s/n]')).upper() .strip()[0]
media = soma/quantidade
print ('A Quantidade de números foram {} e a  media dos valores são {}' .format(quantidade, media))