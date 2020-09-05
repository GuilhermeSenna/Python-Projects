#Jokenpo
from random import choice
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'vermelho':'\033[31m'}
CPU = choice(['PEDRA','PAPEL','TESOURA'])
print(CPU)
PLAYER = input('Escolha pedra, papel ou tesoura: ').upper()
if CPU == PLAYER:
    print('{}Empate{}, Você e o computador escolheram {}.'.format(cores['amarelo'],cores['limpa'],CPU))
elif CPU == 'PEDRA' and  PLAYER == 'TESOURA':
    print('{}perdeste{}, Você escolheu Tesoura e o computador escolheu Pedra.'.format(cores['vermelho'],cores['limpa']))
elif CPU == 'TESOURA' and PLAYER == 'PEDRA':
    print('{}Ganhaste{}, Você escolheu Pedra e o computador escolheu Tesoura.'.format(cores['verde'],cores['limpa']))
elif CPU == 'PAPEL' and PLAYER == 'PEDRA':
    print('{}perdeste{}, Você escolheu Pedra e o computador escolheu Papel.'.format(cores['vermelho'],cores['limpa']))
elif CPU == 'PEDRA' and PLAYER == 'PAPEL':
    print('{}Ganhaste{}, Você escolheu Papel e o computador escolheu Pedra.'.format(cores['verde'], cores['limpa']))
elif CPU == 'TESOURA' and PLAYER == 'PAPEL':
    print('{}perdeste{}, Você escolheu Papel e o computador escolheu Tesoura.'.format(cores['vermelho'], cores['limpa']))
elif CPU == 'PAPEL' and PLAYER == 'TESOURA':
    print('{}Ganhaste{}, Você escolheu Tesoura e o computador escolheu Papel.'.format(cores['verde'], cores['limpa']))
else:
    print('Opcao escolhida invalida.')