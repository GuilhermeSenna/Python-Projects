from random import randint
#sorteado = int(uniform(0,6))
sorteado = randint(0,5)
escolha = int(input('Um numero foi sorteado, tente adivinhar(de 0 a 5): '))
if sorteado == escolha:
    print('Parabens, você acertou, o numero sorteado foi o {}'.format(escolha))
else:
    print('Infelizmente você errou, o numero sortedo foi o {}'.format(sorteado))
    print('e o escolhido por você foi o {}, tente novamente.'.format(escolha))
