def leiaDinheiro(p):
    valido = False
    while not valido:
        entrada = input(p).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
