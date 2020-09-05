lista  = []
resp = 'S'
while resp == 'S':
    x = int(input('Digite um valor: '))
    if len(lista) == 0:
        lista.append(x)
        print('Valor adicionado com sucesso!!')
    else:
        if x in lista:
            print('Valor duplicado, não posso adicionar.')
        else:
            lista.append(x)
            print('Valor adicionar com sucesso!!')
    resp = input('Deseja continuar? [S/N]: ').upper()
    while resp != 'S' and resp != 'N':
        resp = input('Tente novamente, Deseja continuar? [S/N]: ').upper()
print(f'Os valores digitados foi {lista}')