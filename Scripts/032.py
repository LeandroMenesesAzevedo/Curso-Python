print ( '==========  Origem dos anos ==========')

ano = int( input ( ' Digite o ano que deseja: '))

if ano % 4 == 0 and ano % 100 != 0:
    print (' O ano é bissexto')
else:
    if ano % 400 == 0:
        print (' O ano é bissexto')
    else:
        print (' O ano não é bissexto')

