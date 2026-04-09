from datetime import date # utilizado para pegar o ano atual.
print ('Confederação Nacional de Natação')

nasc = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year # pegando o ano atual
idade = atual - nasc

if idade <= 9:
    print ('Sua Classificação é Mirim.')
elif idade > 9 and idade <= 14:
    print (' Sua Classificação é Infatil')
elif idade > 14 and idade <= 19:
    print (' Sua Classificação é Junior')
elif idade > 19 and idade <= 25:
    print (' Sua Classificação  é Sênior')
elif idade > 25:
    print('Sua Classificação é Master')
