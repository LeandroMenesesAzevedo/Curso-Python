maior = 0
menor = 0
for c in range (0, 7):
    idade = int(input('Digite o ano que você nasceu: '))
    midade = 2026 - idade 

if (midade >= 18):
    maior += midade
    print('São pessoas {} maior de idade.'.format(maior))
else:
    if (midade <= 18):
        menor += midade
        print('São pessoas {} menor de idade.'.format(menor))