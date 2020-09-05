numero = int(input('Digite um numero: '))
milhar = numero//1000
resto = numero%1000
centena = resto//100
resto %= 100
dezena = resto//10
unidade = resto%10
print(f'O numero digitado foi {numero}')
print(f'unidade: {unidade}\ndezena: {dezena}\ncentena: {centena}\nmilhar: {milhar}')



