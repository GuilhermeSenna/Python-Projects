def leiaInt(num):
    cores = {'Limpa': '\033[m',
             'vermelho': '\033[31m'}
    while not num.isnumeric():
        print('{}ERRO! Digite um número inteiro válido.{}'.format(cores['vermelho'],cores['Limpa']))
        num = input('Digite um numero: ')
    return num

n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o numero {n}')