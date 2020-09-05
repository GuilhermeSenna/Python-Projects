preco = int(input('Digite o preço do produto: '))
forma = int(input('Digite o formato de pagamento'
                  '\n1 - à vista (10% de desconto).'
                  '\n2 - à vista no cartao (5% de desconto).'
                  '\n3 - em até 2x no cartão (preço normal).'
                  '\n4 - 3x ou mais no cartão (20% de juros).'
                  '\n->'))
if forma == 1:
    print(f'O valor a vista com 10% de desconto fica {preco*0.9} reais.')
elif forma == 2:
    print(f'O valor a vista no cartão com 5% de desconto fica {preco*0.95} reais.')
elif forma == 3:
    print(f'O valor em até 2x no cartão continua o mesmo, {preco} reais.')
elif forma == 4:
    print(f'O valor em 3x ou mais no cartão fica com 20% de juros, {preco*1.2} reais.')
else:
    print('Valor não permitido.')