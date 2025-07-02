print ( ' ALUGUEL DE CARROS ' )
car = int( input (' Quantos dias deseja ficou com carro: ' ))
km = float ( input ( 'Quantos KM foi rodado: ' ))

total = ( car * 60 ) + ( km * 0.15)

print ( 'O valor total a pagar é: {}'.format(total) )
