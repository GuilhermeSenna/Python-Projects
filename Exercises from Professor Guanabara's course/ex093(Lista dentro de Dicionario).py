jogo = {}
gols = []
soma = 0
jogo['nome'] = input('Nome do Jogador: ')
partidas = int(input('Quantas partidas ele jogou: '))
for c in range(0, partidas):
    gols.append(int(input(f' Quantos gols na {c+1}ª partida: ')))
    soma += gols[c]
jogo['gols'] = gols
jogo['total'] = soma
print('=' * 30)
for k, v in jogo.items():
    print(f'O campo {k} tem valor {v}.')
print('=' * 30 )
print('O jogador {} jogou {} partidas'.format(jogo['nome'],partidas))
for pos, n in enumerate(gols):
    print(f'=> Na {pos+1}ª partida, fez {n} gols.')
