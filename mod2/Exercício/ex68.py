n = m = 0
y = 1
while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    elif n > 0:
        while y <= 10:
            m = n * y
            print(f'{n} X {y} = {m}')
            y += 1

print ('Não aceito números negativos para está tabuada.')
