frase = str(input('Digite o seu nome completo: ')).strip()
# Essa função strip informa que essa string virar sem espaço antes e depois
print (frase)
print ('Todas as letras do seu nome com letra maiúscula:')
print (frase.upper())
print ('Todas as letra do seu nome com letra minúscula:')
print (frase.lower())
print ('Quantidade de letra do primeiro nome :')
print ('O Tamanho do texto sem espaço é: {}'.format(len(frase) - frase.count(' ')))
# Como podemos observar ultilizei a função len - count para retirar contar o tamanho do nome sem espaço no meio
# função count conta os espaço
#print('Seu primeiro nome tem {} letras'.format(frase.find(' ')))
separa = frase.split()
#ultilizamos a função split para separa as palavras da frase e colocar em uma lista
#chamamo o separa na posição 0 que mostra o primeiro nome.
print('Seu primeiro nome é {} e ele possui {} letras'.format(separa[0], len(separa[0])))


