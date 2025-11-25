casa = float (input ('Qual o valor do imóvel: '))
sal = float (input ('Qual o seu salário: '))
meses = int (input('Quantos meses deseja pagar: '))


parcela = casa * ( 0.5 * (1 + 0.5)** meses) / (( 1 + 0.5)** meses -1)

if sal < pm:
    parcela = casa * ( 0.5 * (1 + 0.5)** meses) / (( 1 + 0.5)** meses -1)
    print (' O valor da parcela será R$ {:.2f} em {} anos'.format(parcela, ano))
    print (' O financiamento ocorre um juros de 5%')

elif sal > pm:
    print('Seu emprestímo foi negado.')
    print(' Infelizmente você não poderá financiar está casa')
