from math import hypot
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
#print('O Cateto oposto vale {} o cateto adjacente vale {} logo a hipotenusa vale {}'.format(co, ca, sqrt(pow(co, 2) + pow(ca, 2))))
print('O Cateto oposto vale {}, o cateto adjacente vale {} logo a hipotenusa vale {}.'.format(co, ca, hypot(co, ca)))
