total = totprod = maior = menor = cont = 0
barato = ''
while True:
    produto = str(input(' Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    totprod += 1
    cont += 1
    if valor == 0:
            print('*** Valor inválido***')
            break
    if valor > 0:
            total += valor 
    if valor > 1000:
          maior += 1
    if cont == 1:
          menor = valor
          barato = produto
    else:
          if valor < menor:
                menor = valor
                barato = produto 
    resp = str (input('Deseja adicionar outros produtos no carrinho [S/N]: ')).strip()[0] .upper()
    if resp == 'N':
        break
    
print('='*20)
print ('Compra Finalizada')
print(f'Seu Carrinho possui {totprod} produtos')
print(f'O valor total da compra é: R${total:.2f}')
print (f'Produtos acima de R$ 1000.00 = {maior}')
print(f'O produto de menor valor custa R${menor:.2f} nome do produto {barato}')
print('='*20)