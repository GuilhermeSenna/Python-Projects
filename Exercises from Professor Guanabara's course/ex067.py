vazio = ''
while True:
    x = 1
    n = int(input('Quer ver a tabuada de qual valor: '))
    print(f'{vazio:-^30}')
    if n < 0:
        break
    else:
        while x <= 10:
            print(f'{n} x {x} = {n*x}')
            x += 1
    print(f'{vazio:-^30}')