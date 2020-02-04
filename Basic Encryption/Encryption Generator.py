# encryption using randomly generated unique key and Caesar cipher

import os.path
from random import randint

def codificar(alfabeto, arquivo_original, chave, arquivo_codificado, chaves):
    manipulador = open(arquivo_original, 'r')
    mensagem = manipulador.read().strip()
    manipulador.close()
    if tipo == 1:
        codificado = str(chave)
        for i in mensagem:
            if i != ' ':
                if i.isupper():
                    maiuscula = 1
                else:
                    maiuscula = 0
                posicao = alfabeto.index(i.lower())
                aux = (chave + posicao) % 26
                if maiuscula == 1:
                    codificado += alfabeto[aux].upper()
                else:
                    codificado += alfabeto[aux]
            else:
                codificado += ' '
    else:
        cod = ''
        for i in mensagem:
            if i != ' ':
                if i.isupper():
                    maiuscula = 1
                else:
                    maiuscula = 0
                chaves.append(randint(0, 25))
                tam = len(chaves) - 1
                posicao = alfabeto.index(i.lower())
                aux = (chaves[tam] + posicao) % 26 #Resto da divisao
                if maiuscula == 1:
                    cod += alfabeto[aux].upper()
                else:
                    cod = cod + alfabeto[aux]
            else:
                cod = cod + ' '
        codificado = ''
        for c in chaves:
            if c < 10:
                codificado += '0'
                codificado += str(c)
            else:
                codificado += str(c)
        codificado += cod
    manipulador = open(arquivo_codificado, 'w+')
    manipulador.write(codificado)
    manipulador.close()
    print(f'\nMensagem codificada (inserida no arquivo) = {codificado}\n')

def decodificar(alfabeto, arquivo_codificado):
    manipulador = open(arquivo_codificado, 'r')
    mensagem = manipulador.read()
    manipulador.close()
    descodificado = ''
    chave = ''
    if tipo == 1:
        for i in mensagem:
            if i.isnumeric():
                chave = str(chave)
                chave += i
                chave = int(chave)
            else:
                if i != ' ':
                    if i.isupper():
                        maiuscula = 1
                    else:
                        maiuscula = 0
                    posicao = alfabeto.index(i.lower())
                    aux = (posicao - chave) % 26
                    if maiuscula == 1:
                        descodificado += alfabeto[aux].upper()
                    else:
                        descodificado += alfabeto[aux]
                else:
                    descodificado += ' '
    else:
        cont = 0
        contaux = 0
        aux = ''
        newchaves = []
        for i in mensagem:
            if i.isnumeric():
                aux = str(aux)
                aux += i
                aux = int(aux)
                contaux += 1
                if contaux == 2:
                    newchaves.append(aux)
                    aux = ''
                    contaux = 0
            else:
                if i != ' ':
                    if i.isupper():
                        maiuscula = 1
                    else:
                        maiuscula = 0
                    posicao = alfabeto.index(i.lower())
                    aux = (posicao - newchaves[cont]) % 26
                    if maiuscula == 1:
                        descodificado += alfabeto[aux].upper()
                    else:
                        descodificado += alfabeto[aux]
                    cont += 1
                else:
                    descodificado += ' '
    print(f'\nMensagem decodificada = {descodificado}\n')

#Programa principal

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
chaves = [] #Para uso na cifra única
cores = {'Limpa':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[32m'}

#Aqui os nomes dos arquivos podem ser mudados à escolha do usuário, desde que existam e tenham esse nome.
arquivo_original = 'codificar.txt'
arquivo_codificado = 'decodificar.txt'

#Primeiro uso - Caso já exista o arquivo "decodificar.txt" ele irá apagar, para ser criado dentro da função codificar.
if os.path.exists(arquivo_codificado):
    os.remove(arquivo_codificado)

while 1:

    if not os.path.exists(arquivo_original):
        print('\n{} O arquivo de nome "{}" não existe na máquina.{}'.format(cores['vermelho'], arquivo_original, cores['Limpa']))
        break

    elif not os.path.exists(arquivo_codificado):
        print('\n{}Arquivo "{}" reconhecido com sucesso!!{}'.format(cores['verde'], arquivo_original, cores['Limpa']))
        print('{}O arquivo de nome "{}" não existe na máquina (ou foi deletado por ser o primeiro uso), logo só poderá ser possível codificar\n{}'.format(cores['vermelho'], arquivo_codificado, cores['Limpa']))
        escolha = int(input('Deseja codificar ou decodificar a frase? \n0 - Codificar\n1 - Sair do programa\n-> '))

        while escolha != 0 and escolha != 1:
            print('\n' * 130)
            escolha = int(input('Tente Novamente.\nDeseja codificar ou decodificar a frase? \n0 - Codificar\n1 - Sair do programa\n-> '))

        if escolha == 0:
            tipo = int(input('\nDeseja usar:\n1)Cifra de césar com chave escolhida?\n2)Chave única gerada aleatoriamente?\n-> '))
            while tipo != 1 and tipo != 2:
                tipo = int(input('\nTente Novamente.\nDeseja usar:\n1)Cifra de césar com chave escolhida?\n2)Chave única gerada aleátoriamente?\n->'))
            if tipo == 1:
                chave = int(input('\nQual a chave deseja escolher? (0 para manter o original)\n-> '))
                while chave < 0 or chave > 25:
                    print('\n' * 130)
                    chave = int(input('\nQual a chave deseja escolher? 25 >= chave >= 0 (0 para manter o original)\n-> '))
                codificar(alfabeto, arquivo_original, chave, arquivo_codificado, chaves[:])
            else:
                codificar(alfabeto, arquivo_original, 0, arquivo_codificado, chaves[:])
        else:
            break
    else:
        escolha = int(input('Deseja codificar ou decodificar a frase? \n0 - Codificar\n1 - Decodificar\n2 - Sair do programa\n-> '))
        while escolha != 0 and escolha != 1 and escolha != 2:
            print('\n' * 130)
            escolha = int(input('Tente Novamente.\nDeseja codificar ou decodificar a frase? \n0 - Codificar\n1 - Decodificar\n2 - Sair do programa\n-> '))

        if escolha == 0:
            tipo = int(input('\nDeseja usar:\n1)Cifra de césar com chave escolhida?\n2)Chave única gerada aleátoriamente?\n-> '))
            while tipo != 1 and tipo != 2:
                tipo = int(input('\nTente Novamente.\nDeseja usar:\n1)Cifra de césar com chave escolhida?\n2)Chave única gerada aleátoriamente?\n->'))
            if tipo == 1:
                chave = int(input('\nQual a chave deseja escolher? (0 para manter o original)\n-> '))
                while chave < 0 or chave > 25:
                    print('\n' * 130)
                    chave = int(input('\nQual a chave deseja escolher? 25 >= chave >= 0 (0 para manter o original)\n-> '))
                codificar(alfabeto, arquivo_original, chave, arquivo_codificado, chaves[:])
            else:
                codificar(alfabeto, arquivo_original, 0, arquivo_codificado, chaves[:])

        elif escolha == 1:
            decodificar(alfabeto, arquivo_codificado)

        else:
            break
