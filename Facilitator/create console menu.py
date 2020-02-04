def mostralinha(frase):
    print('=-' * 25)
    print(f'{frase:^50}')
    print('=-' * 25)


def menu(frase, *Sitens, sair = False): #Frase a ser mostrada e as opções a serem escolhidas
    '''
    :param frase: Frase para ser mostrada ao usuario para ele escolher. Ex: "Escolha dentre as opções".
    :param Sitens: Opções a serem mostradas ao usuario.
    :param sair: Coloca a opção de sair do programa (por Default é True).
    :return: Caso a opção sair esteja ativada, se o usuário decidir sair OU escolha uma opção fora dos parâmetros
    o return será -1, caso contrário OU a opção esteja desativada, o retorno será a opção escolhida.
    Exemplo de uso: menu('Escolha dentre as opções', 'opção A', 'Opção B', 'Opção C')
        >> Caso use dessa forma a opção sair estará ativada por Default, para desativar acrescente
        False após a última opção. <<
    '''
    mostralinha(frase)
    for k, v in enumerate(Sitens):
        print(f'{k+1}) {v}')
    if sair == True:
        print(f'{k+1}) Sair do menu')
        print(f'>>  Qualquer opção junto da {k+1} fara o programar sair. <<')
    resp = input('->')
    while True:
        try:
            int(resp)
        except(ValueError, TypeError):
            resp = input('Digite Um valor inteiro dentre as opções\n->')
            continue
        else:
            resp = int(resp)
            if sair == True:
                if resp < 1 or resp > k:
                    return -1
                else:
                    return resp
            else:
                return resp


menu('pular ou não', 'sim', 'não', 'talvez', True)
