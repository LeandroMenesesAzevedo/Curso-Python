print ('========================= Loja de Tintas ==============================')

larg = float(input('Digite a largura da parede : '))
alt = float(input('Digite a altura da parade : '))

area = alt * larg
litro = 1 / 2 # A cada um litro de tinta é possivel pintar uma area de 2m²

valor = area * litro # valor final de quantos litros de tinta

print('A area é {}'.format(area))
print('Você precisa {} litros de tinta para pintar a area '.format(valor))