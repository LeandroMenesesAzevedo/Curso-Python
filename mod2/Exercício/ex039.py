print ('*********** Sistema de alistamento *************')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade == 18:
    print ('Será necessário se alistar.')

elif idade > 18:
    print ('Já se alistou?')
    print ('Se sim, apresente o certificado de reservista.')

else:
    print ('Você ainda não possui idade suficiente para se alistar.')