a = int(input('Digite o segmento A de um possível triângulo: '))
b = int(input('Digite o segmento B de um possível triângulo: '))
c = int(input('Digite o segmento C de um possível triângulo: '))
if a+b > c and a+c > b and a+c > b:
    print('Os segmentos digitados podem formar um triângulo.')

    if a == b and a == c:
        print('O triangulo é equilatero (todos os lados iguais).')
    elif a == b or a == c:
        print('O triangulo é isosceles (dois lados iguais).')
    else:
        print('O triangulo é escaleno (todos os lados diferentes).')
else:
    print('Os segmentos digitados NAO podem formar um triângulo.')
