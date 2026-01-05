casa = float (input ('Qual o valor do imóvel: '))
sal = float (input ('Qual o seu salário: '))
anos = int (input('Quantos meses deseja pagar: '))
parcela = casa / (anos * 12)
minimo = sal *30 / 100
if parcela <= minimo:

    print (' O valor da parcela será R$ {:.2f} em {} anos'.format(parcela, anos))
    print (' Emprestimo CONCEDIDO')

else:
    print('Seu emprestímo foi negado.')
    print(' Infelizmente você não poderá financiar está casa')
