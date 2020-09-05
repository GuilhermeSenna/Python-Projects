numero = int(input('Digite um numero inteiro: '))
base = int(input('Digite a base de conversão desejada:'
      '\n1 para binário'
      '\n2 para octal'
      '\n3 para hexadecimal.\n->'))
if base == 1:
    print('O numero {} na base binária é {}'.format(numero,bin(numero)[2:]))
elif base == 2:
    print('O numero {} na base octal é {}'.format(numero,oct(numero)[2:]))
elif base == 3:
    print('O numero {} na base hexa é {}'.format(numero,hex(numero)[2:]))
else:
    print('opcao invalida.')
