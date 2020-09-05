media = float(input('Digite a sua média obtida: '))
if media < 5:
    print('Infelizmente você foi reprovado.')
elif media >= 5 and media < 7:
    print('Você ficou de recuperação.')
else:
    print('Parabéns, você foi aprovado.')