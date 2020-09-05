print('Soma dos numeros impares e multiplos de 3:')
soma = 0
for n in range(1,501):
    if n%2 == 1 and n%3 == 0:
        soma += n
print(f'A soma resultante é {soma}')
