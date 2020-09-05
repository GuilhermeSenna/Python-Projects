palavra = input('Digite a palavra desejada: ').upper().replace(" ","")
print(palavra)
reverso = palavra[::-1]
if palavra == reverso:
    print('A palavra digitada é um palindromo.')
else:
    print('A palavra digitada não é um palindromo.')
