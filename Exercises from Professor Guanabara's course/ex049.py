n = int(input('Digite um valor para descobrir a tabuada: '))
print('---------- Tabuada da soma ----------')
for x in range(1, 11):
    print(f'{n}+{x} = {n+x}')
print('---------- Tabuada da multiplicação --------')
for x in range(1, 11):
    print(f'{n}*{x} = {n*x}')