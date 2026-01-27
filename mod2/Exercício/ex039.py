print ('*********** Sistema de alistamento *************')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade == 18:
    print ('Será necessário se alistar.')

elif idade > 18:
    print ('Já se alistou?')
    print ('Se sim, apresente o certificado de reservista.')

else:
    saldo = 18 - idade 
    print ('Você ainda não possui idade suficiente para se alistar.')
    print ('Retorne o alistamento da a {} anos.' .format(saldo))