matriz = [[], [], []]
vazio = ''
soma = 0
somat = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i},{c}]: ')))
print(f'{vazio:-^30}')
for i in range(0, 3):
        for c in range(0, 3):
                if matriz[i][c] % 2 == 0:
                    soma += matriz[i][c]
                if c == 2:
                    somat += matriz[i][c]
                print(f'[{matriz[i][c]:^5}]', end='')
        print()
print(f'A soma de todos os valores pares é {soma}.')
print(f'A soma de todos os valores da terceira coluna é {somat}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}')