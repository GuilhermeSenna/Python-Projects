from random import randint
vitorias = 0
vazio = ''
while True:
    soma = 0
    print(f'{vazio:-^30}\nVamos jogar Par ou impar\n{vazio:-^30}')
    n = int(input('Digite um valor: '))
    escolha = input('Deseja Par/Impar? [P/I] ').upper()
    PC = randint(0, 10)
    soma = n + PC
    print(f'{vazio:-^30}\nVoce jogou {n} e o computador escolheu {PC}, total: {soma}\n{vazio:-^30}')
    if soma %2 == 0:
        if escolha == 'P':
            print('Parabens! Voce ganhou!\nVamos jogar de novo.')
            vitorias += 1
        else:
            print(f'GAME OVER! você perdeu apos vencer {vitorias} vezes.')
            break
    else:
        if escolha == 'I':
            print('Parabens! Voce ganhou!\nVamos jogar de novo.')
            vitorias += 1
        else:
            print(f'GAME OVER! você perdeu apos vencer {vitorias} vezes.')
            break
