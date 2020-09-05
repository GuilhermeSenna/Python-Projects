def mostraLinha():
    print('-' * 50)

def voto(ano):
    idade = 2019 - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 18:
        return 'NÃO PODE VOTAR.'
    elif idade >= 18 and idade < 65:
        return 'VOTO OBRIGATORIO.'
    else:
        return 'VOTO OPCIONAL.'


mostraLinha()
ano = int(input('Digite o seu ano de nascimento: '))
print(voto(ano))