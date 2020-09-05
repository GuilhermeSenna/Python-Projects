#Fatorial
x = int(input('Digite um numero (maior que 0) para descobrir seu fatorial: '))
y = x
fat = 1
while x != 1:
    fat = x * fat
    x -= 1
print(f'O fatorial de {y} é {fat}.')