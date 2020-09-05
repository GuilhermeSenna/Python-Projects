x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))

resp =int(input('Menu de operacoes: '
      'Digite o numero desejado para realizar a operação.\n'
      '1) somar\n'
      '2) multiplicar\n'
      '3) qual o maior?\n'
      '4) adicionar novos numeros\n'
      '5) sair do programa\n->'))
while resp != 5:
    if resp == 1:
        print(f'A soma de {x} e {y} é {x+y}\n\n')
    elif resp == 2:
        print(f'A multiplicacao entre {x} e {y} é {x*y}\n\n')
    elif resp == 3:
        if x > y:
            print(f'O maior valor é {x}\n\n')
        else:
            print(f'O maior valor é {y}\n\n')
    elif resp == 4:
        x = int(input('Digite um novo valor: '))
        y = int(input('Digite outro novo valor: '))
        print('\n\n')
    else:
        while resp < 1 or resp > 5:
            resp = int(input(f'Digite um valor entre 1 e 5\n'
                  f'1)Soma\n'
                  f'2)Multiplicacao\n'
                  f'3)Qual o maior?\n'
                  f'4)Adicionar novos numeros\n'
                  f'5) sair do programa.\n->'))

    resp = int(input('Deseja realizar outra função? (digite 5 para sair do programa): '
                     'Digite o numero desejado para realizar a operação.\n'
                     '1) somar\n'
                     '2) multiplicar\n'
                     '3) qual o maior?\n'
                     '4) adicionar novos numeros\n'
                     '5) sair do programa\n->'))