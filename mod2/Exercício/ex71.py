total = totprod = 0
while True:
    produto = str(input(' Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    totprod += 1
    if valor == 0:
            print('*** Valor inválido***')
            break
    if valor > 0:
            total += valor    
    resp = str (input('Deseja adicionar outros produtos no carrinho [S/N]: ')).strip()[0] .upper()
    if resp == 'N':
        break
    
print('='*20)
print ('Compra Finalizada')
print(f'Seu Carrinho possui {totprod} produtos')
print (f'O valor total da compra é: R${total}')
print('='*20)