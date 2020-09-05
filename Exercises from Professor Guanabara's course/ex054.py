maioridade = menoridade = 0
for c in range(0, 7):
    ano = int(input(f'em que ano a {c+1}ª pessoa nasceu?'))
    if 2019 - ano >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f' A quantidade de menores é {menoridade} pessoas e maiores é {maioridade} pessoas.')