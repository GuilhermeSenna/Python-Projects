from time import sleep

def mostraLinha():
    print('-=' * 30)


def maior(* num):
    mostraLinha()
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end = ' ')
        sleep(.3)
    print(f'Foram analisados {len(num)} ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi o {max(num)}')
    else:
        print('A lista está vazia, logo não existe maior valor.')
    mostraLinha()

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
