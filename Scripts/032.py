from datetime import date #importamos uma biblioteca para pegar o ano atual.

print ( '==========  Origem dos anos ==========')
ano = int( input ( ' Digite o ano que deseja: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print (' O ano é bissexto')
else:
    if ano % 400 == 0:
        print (' O ano {} é bissexto'.format(ano))
    else:
        print (' O ano {} não é bissexto'.format(ano))

