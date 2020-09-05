'''tupla = ('arara', 'banana', 'mamute', 'sofa', 'torneira')
for c in range(0,len(tupla)):
    print(f'\nNa palavra {tupla[c]} temos: ', end=' ')
    for n in range(0,len(tupla[c])):
        if tupla[c][n] == 'a':
            print('a', end=' ')
        elif tupla[c][n] == 'e':
            print('e', end=' ')
        elif tupla[c][n] == 'i':
            print('i', end=' ')
        elif tupla[c][n] == 'o':
            print('o', end=' ')
        elif tupla[c][n] == 'u':
            print('u', end=' ')'''
palavras = ('AVIÃO', 'CARRO' , 'FUTEBOL', 'SKATE','PYTHON','JAVA','CHUVA','ARVORE','NATUREZA')
count = 0
for x in range(0,len(palavras)):
    print(f"\nNa palavra {palavras[x]} temos as vogais:", end=' ')
    for i in palavras[x]:
        if i in 'AEIOUÃ':
            print(i,end=' ' )
print('\n')