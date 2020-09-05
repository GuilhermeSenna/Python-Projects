def leiaInt(num):
    while True:
        try:
            int(num)
        except (ValueError, TypeError):
            print('{}ERRO! Digite um número inteiro válido.{}'.format(cores['vermelho'],cores['Limpa']))
            num = input('Digite um numero Inteiro: ')
            continue
        except (KeyboardInterrupt):
            print('O Usuario nao quis digitar o numero.')
            return 0
        else:
            return num


def leiaFloa(num):
    while True:
        try:
            float(num)
        except (ValueError, TypeError):
            print('{}ERRO! Digite um número inteiro real.{}'.format(cores['vermelho'], cores['Limpa']))
            num = input('Digite um numero real: ')
            continue
        except (KeyboardInterrupt):
            print('O Usuario nao quis digitar o numero.')
            return 0
        else:
            return num

cores = {'Limpa': '\033[m',
             'vermelho': '\033[31m'}
n = leiaInt(input('Digite um número inteiro: '))
n2 = leiaFloa(input('Digite um número real: '))
print(f'O número inteiro digitado foi {n} e o real foi {n2}')