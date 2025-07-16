from math import radians , sin, cos,tan
# Correção do exercício adicionei a função radians para os valores radianos.
# inserido a função sin = cálculo seno
# inserido a função cos = cáculo cosseno
# inserido a função tan = cálculo tangente

an = float ( input ( 'Digite o angulo: ' ) )
se = sin(radians(an))
co = cos(radians(an))
ta = tan(radians(an))

print ( 'O angulo digitado foi {:.0f}'.format(an) )
print ( 'O seno é: {:.2f} '.format(se) )
print ( 'O coseno é: {:.2f}'.format(co))
print ( 'A tangete é: {:.2f}'.format(ta) )
