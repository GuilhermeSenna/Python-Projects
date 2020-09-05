a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
if a > b and a > c:
    if b > c:
        print(f'O maior valor é {a} e o menor é {c}')
    else:
        print(f'O maior valor é {a} e o menor é {b}')
elif b > a and b > c:
    if a > c:
        print(f'O maior valor é {b} e o menor é {c}')
    else:
        print(f'O maior valor é {b} e o menor é {a}')
else:
    if a > b:
        print(f'O maior valor é {c} e o menor é {b}')
    else:
        print(f'O maior valor é {c} e o menor é {a}')
