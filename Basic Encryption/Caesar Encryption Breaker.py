# Caesar encryption breaker

import os.path

def decodificar(alfabeto, arquivo):
    manipulador = open(arquivo, 'r')
    mensagem = manipulador.read()
    aux = mensagem
    manipulador.close()
    descodificado = ''
    possiveis = []
    for cont in range(26):
        for i in mensagem:
            if i != ' ':
                if i.isupper():
                    maiuscula = 1
                else:
                    maiuscula = 0
                posicao = alfabeto.index(i.lower())
                aux = (posicao - cont) % 26
                if maiuscula == 1:
                    descodificado += alfabeto[aux].upper()
                else:
                    descodificado += alfabeto[aux]
            else:
                descodificado += ' '
        possiveis.append(descodificado)
        descodificado = ''
    for k,v in enumerate(possiveis):
        print(f'{k+1}-> {v}')


#Programa principal
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
arquivo = 'teste.txt'

if not os.path.exists(arquivo):
    print(f'\nO arquivo de nome {arquivo} não existe na máquina.')
    exit()

decodificar(alfabeto, arquivo)
