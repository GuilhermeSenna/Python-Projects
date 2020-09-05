first = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
i = 1
while i <= 10:
    PA = first + (i-1)*r
    print(f'{PA} -> ',end='')
    i += 1
print('FIM')