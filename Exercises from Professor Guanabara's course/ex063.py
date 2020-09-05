'''i = int(input('Digite a quantidade de elementos desejado da sequencia de fibonnaci (maior que 0): '))
while i <= 0:
    i = int(input('Por favor digite um valor maior que 0: '))
if i == 1:
    print('1')
elif i == 2:
    print('1 -> 1')
else:
    x = y = 1
    print(f'{x} -> {y} -> ', end='')
    c = 3
    while c <= i:
        if c % 2 == 0:
            y += x
            print(f'{y} ->', end='')
        else:
            x += y
            print(f'{x} ->', end='')
        c += 1
print('FIM')'''

Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while n != 0:
    print('{}'.format(Fibonacci), end=' → ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')