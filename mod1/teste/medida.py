print ('============== Conversor Centímetros em Milímetros==================')
md = float(input('Digite a medida em metros: '))

xkm =md /1000
xhm = md/100
dam = md/10
xcm = md * 100
xmm = md * 1000

print('A medida {}m corresponde a'.format(md))
print('{}km'.format(xkm))
print('{}hm'.format(xhm))
print('{}dam'.format(dam))
print('{:.0f}cm'.format(xcm))
print('{:.0f}mm'.format(xmm))