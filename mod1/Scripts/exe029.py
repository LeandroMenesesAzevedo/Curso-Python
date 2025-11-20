print (' ========== Sistema de transito ===========')

vel = float(input('Qual a velocidade atual? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO você passou acima do limite de velocidade da via que é 80km/h')
    print('Você foi multado em R$ {:.2f}'.format(multa))

print ('Tenha um  bom dia e dirija com segurança')