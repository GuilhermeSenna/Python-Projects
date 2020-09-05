extensos = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente novamente, Digite um numero entre 0 e 20: '))
print(f'O numero que você digitou foi {extensos[n]}.')