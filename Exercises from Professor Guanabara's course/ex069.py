maior = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Qual sua idade? '))
    while idade < 0 or idade > 100:
        idade = int(input('Digite uma idade valida: '))
    sexo = input('Digite o seu sexo [M/F]: ').upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite um sexo valido [M/F]: ').upper()
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    resp = input('Deseja continuar? [S/N]: ').upper()
    while resp != 'S' and resp != 'N':
        resp = input('Digite uma resposta valida [S/N]: ').upper()
    if resp == 'N':
        break
print(f'O numero de maiores de idade é {maior}, o numero de homens é {homens} e o numero de mulheres menores de 20 anos é {mulheres}.')
