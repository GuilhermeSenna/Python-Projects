def mostraLinha():
    print('-' * 50)

def area(l,c):
    print(f'A área de um terreno {l}x{c} é de {l*c}m².')

print(' Controle de Terrenos')
mostraLinha()
L = float(input('Largura (m): '))
C = float(input('Comprimento (m): '))
area(L,C)