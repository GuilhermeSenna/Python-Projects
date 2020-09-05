jogo = {}
gols = []
jogadores = []
soma = 0
resp = 'S'
while resp == 'S':
    jogo['nome'] = input('Nome do Jogador: ')
    partidas = int(input('Quantas partidas ele jogou: '))
    for c in range(0, partidas):
        gols.append(int(input(f' Quantos gols na {c+1}ª partida: ')))
        soma += gols[c]
    jogo['gols'] = gols.copy()
    jogo['total'] = soma
    jogadores.append(jogo.copy())
    resp = input('Deseja continuar? [S/N] ').strip().capitalize()
    while resp != 'S' and resp != 'N':
        resp = input('Tente novamente, deseja continuar? [S/N] ').strip().capitalize()
print(jogadores)
print('-=' * 30)
print('cod  nome \t\t\tgols\t\t\ttotal')
print('-'*45)
for pos, n in enumerate(jogadores):
    print('{} \t {} \t\t {!s:<15s} \t {}'.format(pos, n['nome'], n['gols'], n['total']))
print('-'*45)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if dados == 999:
        break
    print('LEVANTAMENTO DO JOGADOR {}:'.format(jogadores[dados]['nome']))
    for pos, n in enumerate(jogadores[dados]['gols']):
        print(f'No jogo {pos} fez {n} gols.')