#ESCOLHER 1 DENTRE AS AMOSTRAS
from random import choice
a = input('Primeiro aluno= ')
b = input('Segundo aluno= ')
c = input('Terceiro aluno= ')
d = input('Quarto aluno= ')
#print(f'{choice([a, b, c, d])}')
lista = [a, b, c, d]
print(f'{choice(lista)}')
