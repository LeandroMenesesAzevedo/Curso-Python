#colocamos o strip para retirar o espaço das frases.
#colocamos o upper para deixa a frase em letras maiuscula.
frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra) 
inverso = ''

for letra in range(len(letra) - 1, -1, -1):
    inverso += [letra]
print (junto , inverso)