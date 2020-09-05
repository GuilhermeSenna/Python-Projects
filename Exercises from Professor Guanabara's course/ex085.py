lista = [[], []]
for c in range(0,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'PARES: {sorted(lista[0])}\nIMPARES: {sorted(lista[1])}')