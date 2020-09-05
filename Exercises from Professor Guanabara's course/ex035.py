a = int(input('Digite o segmento A de um possível triângulo: '))
b = int(input('Digite o segmento B de um possível triângulo: '))
c = int(input('Digite o segmento C de um possível triângulo: '))
if a+b > c and a+c > b and a+c > b:
    print('Os segmentos digitados podem formar um triângulo.')
else:
    print('Os segmentos digitados NAO podem formar um triângulo.')
