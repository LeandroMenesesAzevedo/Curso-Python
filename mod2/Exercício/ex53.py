#colocamos o strip para retirar o espaço das frases.
#colocamos o upper para deixa a frase em letras maiuscula.
frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra) 
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print (junto , inverso)

if (junto == inverso):
    print('Essa frase é palíndrome')
else:
    print ('Essa frase não é palíndrome')    