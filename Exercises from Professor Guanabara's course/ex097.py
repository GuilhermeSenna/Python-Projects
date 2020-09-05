#nome = 'Jose'
#idade = 33
#salario = 936.20
#print(f'o {nome:-^20} tem {idade} anos e ganha R${salario}.') #espaçado 20 centralizado tracejado

def escreve(frase):
    traco = (len(frase)) + 4
    print('~' *traco)
    print(f'  {frase}')
    print('~' *traco)

Frase = "Olá,Mundo!"
escreve("Olá,Mundo!")
escreve("Guilherme Senna Cruz")