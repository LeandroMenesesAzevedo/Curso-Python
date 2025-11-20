


n1 = float  (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('A média final do aluno foi: {}'.format(media))
    print('O aluno está \033[32m APROVADO')

elif media >= 5 and media < 7:
    print('A média final do aluno foi: {}'.format(media))
    print('O aluno está em \033[33m RECUPERAÇÃO')

else:
    print ('A média final do aluno foi: {}'.format(media))
    print ('O aluno está \033[31m REPROVADO')