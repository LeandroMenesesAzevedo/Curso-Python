n = s = cont = 0
while True:
    n = int(input('Digite um número (999 para encerrar): '))
    if n == 999:
        break
    s += n
    cont += 1
print (f'A quantidade de números digitados foi: {cont}')    
print (f'O soma entre os números digitados são: {s} ') 
