n = 0
while True:
    print('-'*20)
    n = int(input('Digite um número: '))
    print('-'*20)
    if n < 0:
        break
    y = 1
    while y <= 10:
        m = n * y
        print(f'{n} X {y} = {m}')
        y += 1

print ('Não aceito números negativos para está tabuada.')
