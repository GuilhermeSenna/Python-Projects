def mostraLinha():
    print('='*40)
    frase = 'RESUMO DO VALOR'
    print(f'{frase:^40}')
    print('='*40)

def resumo(n=0, inc=0, dec=0):
    moeda = 'R$'
    mostraLinha()
    print(f'Preço analisado: \t\t\t\t{moeda}{n:>.2f}'.replace('.', ','))
    print(f'Dobro do preço: \t\t\t\t{moeda}{n*2:>.2f}'.replace('.', ','))
    print(f'Metade do preço: \t\t\t\t{moeda}{n/2:>.2f}'.replace('.', ','))
    aux = n
    n += (n * inc / 100)
    print(f'{inc}% de aumento: \t\t\t\t{moeda}{n:>.2f}'.replace('.', ','))
    n = aux
    n -= (n * dec / 100)
    print(f'{dec}% de redução: \t\t\t\t{moeda}{n:>.2f}'.replace('.', ','))
    print('=' * 40)
