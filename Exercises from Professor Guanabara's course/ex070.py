total = 0
maiores = 0
while True:
    nome = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    while valor < 0:
        valor = float(input('Digite um valor valido: '))
    if total == 0:
        menor = valor
        barato = nome
    else:
        if valor < menor:
            menor = valor
            barato = nome
    total += valor
    if valor > 1000:
        maiores += 1
    resp = input('Deseja continuar? [S/N]').upper()
    while resp != 'S' and resp != 'N':
        resp = input('Digite uma resposta valida: [S/N]').upper()
    if resp == 'N':
        break
print(f'O total gasto foi {total}, São {maiores} produtos que custam mais de 1000 reais e o produto mais barato é {barato}.')
