c = 1
par = impar = 0

while c <= 5:
    if c != 0:
        if c % 2 == 0:
            par +=1
        else:
            impar +=1
print ('Foram digitados {} par e {}impar'.format(par, impar))