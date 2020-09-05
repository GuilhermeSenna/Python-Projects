from time import sleep
from random import randint

def sorteia(lst):
    print("Sorteando 5 valores da Lista: ", end='')
    for c in range(5):
        num = randint(1, 10)
        lst.append(num)
        print(f'{num}', end=' ')
        sleep(.3)
    print('Pronto!')
    SomaPar(lst)

def SomaPar(lst):
    sompar = 0
    for valor in lst:
        if valor%2 == 0:
            sompar += valor
    print(f'Somando os valores pares de {lst}, temos {sompar}')

lista = list()
sorteia(lista)