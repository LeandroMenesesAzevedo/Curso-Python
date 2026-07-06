somaid = 0
media = 0
maioridadehomem = 0
nomevelho = ''

for c in range (1 , 5):
    print ('------ {}º Pessoa -----'.format(c))
    nome = str (input('Nome: ')).strip() # coloquei o strip para tirar os espaços
    idade = int (input('Idade: '))
    sex = str (input ('Sexo [ M/F ]: ')).strip() # coloquei o strip para tirar os espaços
    somaid += idade

    if c == 1 and sex in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    
    if sex in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    

media = somaid/c
print ('A media de idade é : {}'.format(media))
print ('O homem mais velho é {} com {}'.format(nomevelho, maioridadehomem))