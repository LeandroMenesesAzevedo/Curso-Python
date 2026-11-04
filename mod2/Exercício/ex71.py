total = 0
while True:
    produto = str(input(' Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    if valor == 0:
            break
    elif valor < 0:
            total += valor

    resp = str (input('Deseja adicionar outros produtos no carrinho [S/N]: ')).strip()[0] .upper()
    if resp == 'N':
        break
    
print('='*20)
print ('Compra Finalizada')
print (f'O valor total da compra é: R${total}')
print('='*20)