c = 1
while c <= 3 :
    sexo = str (input('Digite seu sexo [ M/F ] -> ')).upper().strip()

    if sexo == 'M' and sexo == 'F':
        print ('{}'.format(sexo))
    else:
        print ('ERRO')


    