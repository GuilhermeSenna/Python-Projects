vazio = ''
print(f'{vazio:-^20} LISTAGEM DE PREÇOS {vazio:-^20}\n')
precos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Mochila', 120, 'Livro', 34.90)
for c in range(0, len(precos),2):
    print(f'{precos[c]}{vazio:.^20}{precos[c+1]:.2f}')