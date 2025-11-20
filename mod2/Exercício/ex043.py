alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (alt * alt)

if imc < 18.5:
    print('Seu IMC é de {:.2f}'.format(imc))
    print('Você está \033[31m ABAIXO DO PESO')

elif imc >= 18.5 and imc < 24.9:
    print ('Seu IMC é de {:.2f}'.format(imc))
    print('Você está no peso \033[32m NORMAL')
elif imc > 25 and imc <29.9:
    print ('Seu IMC é de {:.2f}'.format(imc))
    print ('Você está com \033[33m SOBREPESO')
else:
    print('Seu IMC é de {:.2f}'.format(imc))
    print('Você está com \033[31m OBESIDADE')