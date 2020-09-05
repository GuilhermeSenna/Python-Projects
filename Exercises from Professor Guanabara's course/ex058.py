from random import randint
tentativa = 0
#sorteado = int(uniform(0,6))
sorteado = randint(0, 10)
escolha = int(input('Um numero foi sorteado, tente adivinhar(de 0 a 10): '))
if sorteado == escolha:
    print('Parabens, você acertou de primeira o numero {}'.format(sorteado))
else:
    tentativa += 1
    while sorteado != escolha:
      escolha = int(input('Ops, numero escolhido errado, tente novamente: '))
      tentativa += 1
print('Parabens, voce acertou apos {} tentivas, o numero escolhido fora {}'.format(tentativa,sorteado))