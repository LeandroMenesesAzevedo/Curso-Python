import random 

no1 = str ( input ( 'Digite o primeiro nome: ' ))
no2 = str ( input ( 'Digite o segundo nome: ' ))
no3 = str ( input ( 'Digite o terceiro nome: ' ))
no4 = str ( input ( 'Digite o quarto nome: ' ))

lista = [ no1, no2, no3, no4 ]
random.shuffle(lista)

print (lista)

