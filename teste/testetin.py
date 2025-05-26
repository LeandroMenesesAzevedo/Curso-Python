print ('========================= Loja de Tintas ==============================')

larg = float(input('Digite a largura da parede : '))
alt = float(input('Digite a altura da parade : '))

area = alt * larg

valor = area /2

print('A area é {}'.format(area))
print('Você precisa {} litros de tinta para pintar a area '.format(valor))