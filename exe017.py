from math import hypot
co = float(input('Cumprimento do Cateto Oposto : '))
ca = float(input('Cumprimento do Cateto Adjacente: '))
h1 = hypot(co, ca)
print('A Hipotenusa vai meidr {:.2f} !!'.format(h1))
