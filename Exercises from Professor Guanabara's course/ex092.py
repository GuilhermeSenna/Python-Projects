pessoa = {}
pessoa['nome'] = input('Digite o seu nome: ').strip().capitalize()
ano = int(input('Digite o ano de nascimento: '))
pessoa['idade'] = 2019 - ano
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = float(input('Salario R$ '))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - ano) + 35
print('=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')