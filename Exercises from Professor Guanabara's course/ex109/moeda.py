def metade(n=0, x=True, moeda='R$'):
    if x == True:
        n /= 2
        return f'{moeda}{n:>.2f}'.replace('.', ',')
    else:
        return n/2


def dobro(n=0, x=True, moeda='R$'):
    if x == True:
        n *= 2
        return f'{moeda}{n:>.2f}'.replace('.', ',')
    else:
        return n*2


def aumentar(n=0, quant=0, x=True, moeda='R$'):
    if x == True:
        n += (n*quant/100)
        return f'{moeda}{n:>.2f}'.replace('.', ',')
    else:
        return n + (n*quant/100)


def diminuir(n=0, quant=0, x=True, moeda='R$'):
    if x == True:
        n -= (n*quant/100)
        return f'{moeda}{n:>.2f}'.replace('.', ',')
    else:
        return n + (n*quant/100)