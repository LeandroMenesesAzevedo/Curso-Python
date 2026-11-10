print('='*30)
print('{:^30}'.format('Banco DIN'))
print('='*30)
valor = int(input('Digite o valor que deseja sacar: R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total {totalced} valor das cédulas R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        elif total == 0:
            break