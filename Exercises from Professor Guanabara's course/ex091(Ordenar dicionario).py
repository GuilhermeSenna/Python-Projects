from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'Jogador1' : randint(1, 6),
           'Jogador2' : randint(1, 6),
           'Jogador3' : randint(1, 6),
           'Jogador4' : randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in sorteio.items():
    print(f'\tO {k} tirou {v}')
    sleep(1)
print('\nRanking dos jogadores.\n')
ranking = sorted(sorteio.items(), key = itemgetter(1), reverse=True) # 0 em função de chave, 1 de valor
for k, v in enumerate(ranking):
    print(f'\t{k+1}º lugar: O {v[0]} com {v[1]}.')
    sleep(1)
