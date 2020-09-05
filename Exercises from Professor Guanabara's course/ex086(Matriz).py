matriz = [[], [], []]
vazio = ''
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{c}]: ')))
print(f'{vazio:-^30}')
for i in range(0, 3):
        for c in range(0, 3):
                print(f'[{matriz[i][c]:^5}]', end='')
        print()