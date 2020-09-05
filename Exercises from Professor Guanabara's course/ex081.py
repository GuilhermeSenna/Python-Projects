lista = []
resp = 'S'
while resp == 'S':
    lista.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar [S/N]: ').upper()
    while resp != 'S' and resp != 'N':
        resp = input('Tente novamente, Deseja continuar [S/N]: ').upper()
print(f'A quantidade de valores digitados foi {len(lista)}')
lista.sort(reverse = True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O 5 está na lista.')
else:
    print('O 5 não está na lista.')