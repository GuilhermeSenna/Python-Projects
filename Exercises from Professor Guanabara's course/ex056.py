media = 0
mulheres = 0
for c in range(0, 4):
    print(f'------ {c+1}ª pessoa ------')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo[M/F]: ').upper()
    media += idade
    if c == 0:
        maior = idade
        nomemaior = nome
    else:
        if idade > maior:
            maior = idade
            nomemaior = nome
    if sexo == 'F' and idade < 20:
        mulheres += 1
print('---------------------------')
print(f'A media de idade do grupo é de {media/4} anos.')
print(f'a pessoa mais velha tem {maior} anos e se chama {nome}.')
print(f'Ao todo sao {mulheres} mulheres com menos de 20 anos.')