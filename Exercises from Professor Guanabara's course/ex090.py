aluno = dict()
aluno['nome'] = input('Digite o seu nome: ').strip().capitalize()
aluno['media'] = float(input('Digite a sua media: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'
print('\n')
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')