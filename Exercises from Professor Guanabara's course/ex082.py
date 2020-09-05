lista = []
pares = []
impares = []
resp = 'S'
while resp == 'S':
    lista.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? [S/N]: ').upper()
    while resp != 'S' and resp != 'N':
        resp = input('Tente novamente, deseja continuar? [S/N]: ').upper()
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'\nA lista completa é {lista}')
if len(pares) == 0:
    print('Não há numeros pares.')
else:
    print(f'Os numeros pares são {pares}')
if len(impares) == 0:
    print('Não há numeros impares.')
else:
    print(f'Os numeros impares são {impares}')