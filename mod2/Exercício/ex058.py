sexo = str (input('Digite seu sexo [ M/F ] -> ')).upper().strip()[0] #pegou a primeira letra

while sexo not in 'MmFf': #enquanto o sexo não for masculino e femenino faça
    print(' DADOS INVÁLIDOS. INFORME NOVAMENTE ABAIXO: ')
    sexo = str (input('Digite seu sexo [M/F] -> ')).upper().strip()[0] #pegou a primeira letra

print ('O sexo informado foi {}'.format(sexo))




    