first = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite sua razão: '))
last = first + 9*r
i = 1
for n in range(first, last + first, r):
        print('{}º termo = {}.'.format(i,n))
        i += 1
