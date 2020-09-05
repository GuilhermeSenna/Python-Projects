dados = {}
pessoas = []
resp = 'S'
media = 0
while resp == 'S':
    dados['nome'] = input('Digite o nome: ')
    dados['sexo'] = input('Digite o sexo [M/F] ').upper()
    dados['idade'] = int(input('Digite a idade: '))
    media += dados['idade']
    pessoas.append(dados.copy())
    resp = input('Deseja continuar? [S/N] ').strip().capitalize()
    while resp != 'S' and resp != 'N':
        resp = input('Tente novamente, Deseja continuar? [S/N]').strip().capitalize()
print('=' * 30)
print(pessoas)
media = media/len(pessoas)
print(f'Foram cadastradas {len(pessoas)}.')
print(f'A média da idade do grupo é {media:.2f}.')
print('As mulheres cadastradas foram: ', end='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print('\nLista de pessoas acima da media: ')
for e in pessoas:
    for k, v in e.items():
        if e['idade'] > media:
            print(f'{k} = {v}; ', end='')
