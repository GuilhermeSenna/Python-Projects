def ficha(J = '<desconhecido>', G = 0):
    mostraLinha()
    print(f'O jogador {J} fez {G} gol(s) no campeonato.')

def mostraLinha():
    print('\n')
    print('-' * 50)


jogador = input('\nNome do Jogador: ')
gols = input('Numero de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(G = gols)
else:
    ficha(jogador, gols)