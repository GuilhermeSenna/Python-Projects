#soma de 6 numeros inteiros (somente pares)
soma = 0
for x in range(0, 6):
    n = int(input(f'{x+1})Digite um valor inteiro: '))
    if n%2 == 0:
        soma += n
print(f'A soma dos numeros pares digitados é: {soma}')
