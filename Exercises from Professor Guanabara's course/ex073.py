ranking = ('Flamengo', 'América', 'Atlético-PR', 'Atletico-MG', 'Bahia', 'Botafogo', 'Chapecoense', 'Corinthians', 'Cruzeiro', 'Fluminense', 'Grêmio', 'Internacional', 'Palmeiras', 'Ponte', 'Santos', 'Sport', 'São Paulo', 'Vasco', 'Vitória', 'Coritiba')
vazio = ''
print(f'\n{vazio:-^30} 5 PRIMEIROS COLOCADOS {vazio:-^30}')
for c in range(0,5):
    print(f'{c+1}){ranking[c]}')
print(f'{vazio:-^30} 4 ULTIMOS COLOCADOS {vazio:-^30}')
x = 17
for n in range(-4,0):
    print(f'{x}){ranking[n]}')
    x += 1
print(f'{vazio:-^30} Em ordem alfabética {vazio:-^30}')
print(sorted(ranking))
print(f'{vazio:-^30} Posição do chapecoense {vazio:-^30}')
print('O chapecoense está em {}ª posição.'.format({ranking.index('Chapecoense')+1}))
