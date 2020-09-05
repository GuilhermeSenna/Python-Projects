from time import sleep


def mostraLinha():
    print('-=' * 30)


def contador(i, f, p):
    mostraLinha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    #sleep(1)
    print(p)
    if i > f and p > 0:
        p = -p
    if p == 0:
        p = 1
    if p > 0:
        for c in range(i, f+1, p):
            print(c, end=' ')
            #sleep(.3)
    else:
        for c in range(i, f-1, p):
            print(c, end=' ')
            #sleep(.3)
    print('Fim!')
    mostraLinha()


contador(1, 10, 1)
contador(10, 0, -2)
print(f'Agora é sua vez de personalizar a contagem!')
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)