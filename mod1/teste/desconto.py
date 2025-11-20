preco = float(input('Qual o Preço do produto: R$ '))
novop = preco - (preco*5/100)

print('O valor do produto é: R${:.2f}'.format(preco))
print('O valor do produto com desconto é: R${:.2f}'.format(novop))
