import math

an = float ( input ( 'Digite o angulo: ' ) )
se = math.sin(an)
co = math.cos(an)
ta = math.tan(an)

print ( 'O angulo digitado foi {:.0f}'.format(an) )
print ( 'O seno é: {:.2f} '.format(se) )
print ( 'O coseno é: {:.2f}'.format(co))
print ( 'A tangete é: {:.2f}'.format(ta) )