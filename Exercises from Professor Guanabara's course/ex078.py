'''lista = []
maxpos = []
minpos = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        menor = maior = lista[c]
        maxpos.append(0)
        minpos.append(0)
    else:
        if lista[c] > maior:
            maior = lista[c]
            del(maxpos)
            maxpos = []
            maxpos.append(c)
        elif lista[c] < menor:
            menor = lista[c]
            del(minpos)
            minpos = []
            minpos.append(c)
        elif lista[c] == maior and lista[c] == menor: #lista com valores iguais
            maxpos.append(c)
            minpos.append(c)
        elif lista[c] == maior:
            maxpos.append(c)
        else:
            minpos.append(c)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições {maxpos}')
print(f'O menor valor digitado foi {menor} nas posições {minpos}')'''

valores = [int(input('Digite o valor para a posição {}: '.format(i))) for i in range(5)]
print('=-' * 30)
print('Você digitou os valores {}: '.format(valores))

maior = max(valores)
menor = min(valores)

print('O maior valor digitado foi o {} nas posições '.format(maior), end='')
for ind, val in enumerate(valores):
    if val == maior:
        print(f'{ind}...', end='')

print('\nO menor valor digitado foi o {} nas posições '.format(menor), end='')
for ind, val in enumerate(valores):
    if val == menor:
        print(f'{ind}...', end='')