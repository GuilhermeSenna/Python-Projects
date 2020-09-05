for c in range(0, 5):
    peso = int(input(f'Digite o peso da {c+1}ª pessoa: '))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O menor peso foi {menor} e o maior peso foi {maior}.')