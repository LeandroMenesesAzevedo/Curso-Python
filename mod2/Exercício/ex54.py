from datetime import date

atual = date.today().year
maior = 0
menor = 0

for c in range (0, 7):
    idade = int(input('Digite o ano que você nasceu: '))
    midade = atual - idade
    
    if midade >= 18:
            maior += 1
    else:
            menor += 1

print ('Ao todo tivemos {} maior de idade'.format(maior))
print ('Ao todo tivemos {} menor de idade'.format(menor))          