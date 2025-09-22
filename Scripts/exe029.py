print (' ========== Sistema de transito ===========')

vel = int(input('Qual a velocidade atual? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado em R$ {:.2f}'.format(multa))
else:
    print ('Parabéns, conduza com segurança.')