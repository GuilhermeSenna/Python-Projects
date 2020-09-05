x = int(input('Digite um valor: '))
soma = 0
digitados = 0
maior = menor = x
resp = input('Deseja continuar? ->').upper()
soma += x
digitados += 1
while resp == 'S':
    x = int(input('Digite outro valor: '))
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
    soma += x
    digitados += 1
    resp = input('Deseja continuar? ->').upper()
print(f'O maior valor é {maior}, o menor é {menor} e a'
      f' media é {soma/digitados}.')