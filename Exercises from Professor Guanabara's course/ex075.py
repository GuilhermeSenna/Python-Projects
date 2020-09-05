#numeros = tuple(int(input('Digite o {}º numero: '.format(i+1)))for i in range(4)) - Resumido
numeros = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print('O numero 3 aparece na posição {}.'.format(numeros.index(3)+1))
else:
    print('Não foi encontrado o valor 3.')
pares = 0
for c in numeros:
    if c % 2 == 0:
        pares += 1
print(f'A quantidade de numeros pares foi {pares}.')