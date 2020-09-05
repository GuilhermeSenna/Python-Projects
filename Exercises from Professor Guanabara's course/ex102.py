def fatorial(numero, show=False):
    fat = 1
    processo = ''
    for c in range(numero, 0, -1):
        fat *= c
        if c != 1:
            processo += str(c) + ' x '
        else:
            processo += str(c) + ' = '
    processo += str(fat)

    if show == True:
        return processo
    else:
        return fat

print(fatorial(4, True))