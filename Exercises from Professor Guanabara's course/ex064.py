digitados = 0
soma = 0
x = int(input('Digite um valor qualquer (digite 999 para sair do programa): '))
while x != 999:
    digitados += 1
    soma += x
    x = int(input('Digite outro valor qualquer (digite 999 para sair do programa): '))
print(f'A quantidade de valores digitados foi {digitados} e a soma deles é {soma}.')
