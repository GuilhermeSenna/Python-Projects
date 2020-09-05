lista = []
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0:
        lista.append(x)
    else:
        for pos, n in enumerate(lista):
            if x < n:
                lista.insert(pos, x)
                break
            elif len(lista) == pos+1:
                lista.append(x)
                break
print(f'Os cinco valores digitados são: {lista}')