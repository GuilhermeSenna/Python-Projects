'''from random import randint
from time import sleep
vazio = ''
unico = []
lista = []
print(f'{vazio:-^50}\n\t\t\t\tJOGO NA MEGA SENA\n{vazio:-^50}')
jogos = int(input('Quantos deseja que eu sorteie: '))
print(f'\n{vazio:=^50}\n\t\t\t\t SORTEANDO {jogos} JOGOS.\n{vazio:=^50}')
for c in range(0, jogos):
    for n in range(0, 6):
        m = randint(1, 60)
        if not unico:
            unico.append(m)
        else:
            while m in unico:
                m = randint(1, 60)
            unico.append(m)
    unico.sort()
    lista.append(unico[:])
    unico.clear()

for pos, l in enumerate(lista):
    print(f'{pos+1}) jogo: {l}')
    sleep(0.5)
print(f'\n{vazio:=^50}\n\t\t\t\t BOA SORTE.\n{vazio:=^50}')'''

from random import sample
from time import sleep
jogos=list()
n=int(input('Quantos jogos?: '))
for c in range(n):
  a=sorted(sample(range(1, 61), 6)) #Nao se repetem
  jogos.append(a[:])
  print(f'Jogo {c+1}: {a}')
  sleep(0.5)