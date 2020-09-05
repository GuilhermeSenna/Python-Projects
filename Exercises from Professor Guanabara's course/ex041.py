ano = int(input('Digite o seu ano de nascimento: '))
idade = 2019 - ano
if idade <= 9:
    print('Sua categoria é a MIRIM.')
elif idade <= 14:
    print('Sua categoria é a INFANTIL.')
elif idade <= 19:
    print('Sua categoria é a JUNIOR.')
elif idade == 20:
    print('Sua categoria é a SENIOR.')
else:
    print('Sua categoria é a MASTER.')