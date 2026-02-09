print ('{:=^40}'.format(' Loja do Chapéu ')) 

compra = float (input ('Digite o valor da compra: R$ '))

print (''' Formas de Pagamento:
       [1] - à vista dinheiro ou cheque
       [2] - à vista cartão
       [3] - 2x no cartão 
       [4] - 3x ou mais no cartão
''')

opcao = int(input(' Escolha uma opção: '))

if opcao == 1:
    desconto = compra * 0.10
    valor = compra - desconto
    print (' O valor foi pago à vista ')
    print (' Houve um desconto de R${:.2f} total a pagar R${:.2f}'.format(desconto , valor))

