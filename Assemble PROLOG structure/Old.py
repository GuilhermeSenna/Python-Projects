import os
cidades = list()
trajeto = input('Digite a rota por ordem (partida até o destino) ->').split()
rota = trajeto[0]+"x"+trajeto[len(trajeto)-1]
for c in range(len(trajeto)-1):
    dist = float(input(f'Digite a distancia entre {trajeto[c]} e {trajeto[c+1]} = '))
    cidades.append(f'distancia({trajeto[c]}, {trajeto[c+1]}, {dist}).')

print('\n')
for c in cidades:
    print(c)

os.system("pause")