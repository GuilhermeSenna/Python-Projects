# PRISM Mining not finished
# -> does not generate rules
# -> does not read from file

from sys import exit


def tabela():
    # Printa o cabeçalho
    print('\n')
    for c in range(len(PRISM)):
        print(f'{variaveis[c]}\t', end='')
    print('\n')

    for c in range(len(PRISM[0])):
        for n in range(len(PRISM)):
            print(f'{PRISM[n][c]}\t\t', end=' ')
        print('\n')


def checar(aux):
    for c in range(len(PRISM)):
        if c == 0:
            aux = len(PRISM[c])
        if len(PRISM[c]) != aux:
            print('\n>> As variaveis tem tamanhos diferentes, modifique isso <<')
            exit()


def funcao_ini(c, n):
    aux2.clear()
    aux2.append(variaveis[c])  # Adiciona a variavel na qual ele pertence
    aux2.append(PRISM[c][n])  # Adiciona o valor da variavel
    aux2.append(1)  # Adiciona o valor 1, pois so tem 1 ainda
    aux2.append(0)  # Adiciona o 0 por padrão
    Quantidade.append(aux2[:])  # Adiciona a copia da lista na lista de lista
    aux2.clear()  # Limpa a lista auxiliar
    if PRISM[len(PRISM)-1][n] == valor_esperado: # Se corresponde a 'sim'
        Quantidade[len(Quantidade) - 1][3] += 1


def funcao_quantidade(flag):
    for c in range(len(PRISM)-1):                                    # Percorre as colunas
        for n in range(len(PRISM[c])):                               # Percorre as linhas
            if n == 0:                                               # Caso 1 = Primeiro linha examinada
                funcao_ini(c, n)                                     # Chama função auxiliar
            else:
                for k in range(len(Quantidade)):                     # Caso 2 = O Valor já está na tabela
                    if PRISM[c][n] in Quantidade[k]:                 # Se já possuir esse valor
                        flag = 1                                     # Flag para sinalizar que já possui
                        Quantidade[k][2] += 1                        # Incrementa quantas vezes o valor aparece
                        if PRISM[len(PRISM)-1][n] == valor_esperado: # Se o valor da o valor esperado
                            Quantidade[k][3] += 1                    # Incrementa a quantidade de vezes do valor esperado
                if flag == 0:                                        # Caso 3 = Esse valor ainda não foi inserido
                    funcao_ini(c, n)                                 # Chama função auxiliar
            flag = 0


def estatisticas():
    aux2.clear()
    min = 1  # Não tem como a probabilidade ser maior que 1, logo vai achar os valores menores
    print(Quantidade)
    for c in range(len(Quantidade)):  # Substituir a quantidade dos itens pela probabilidade deles
        print(f'{Quantidade[c][1]} tem a probabilidade de {Quantidade[c][3] / Quantidade[c][2]:.3f} de dar "{valor_esperado}". ')
        aux2.append(Quantidade[c][1])
        aux2.append(Quantidade[c][3] / Quantidade[c][2])
        if Quantidade[c][3] / Quantidade[c][2] <= min:
            min = Quantidade[c][3] / Quantidade[c][2]
    return min


def criando_regra():
    aux = aux2.index(min) - 1  # Posição com a variavel de menor probabilidade
    valor = aux2[aux]  # Recebe String

    for k, v in enumerate(PRISM):
        if v.count(valor) > 0:  # Buscando a variavel com o menor valor desejado
            aux2.clear()
            for x, y in enumerate(v):
                if y == valor:
                    aux2.append(x)

    for c in range(len(PRISM)):
        count = 0
        for k, v in enumerate(aux2):
            PRISM[c].pop(v - count)
            count += 1


''' Exemplo de como funciona a PRISM

    Coluna 1             | Coluna 2           | Coluna 3
    Estuda pra prova     | Fez atividades     | Passa na materia
    Não estuda pra prova | Não faz atividades | Não passa na matéria
    
    AS COLUNAS DEVEM TER A MESMA QUANTIDADE, CASO CONTRÁRIO O PROGRAMA INFORMARÁ E SE FECHARÁ.
    
    Da coluna 1 e 2 será obtidas os requisitos para se chegar no resultado esperado na coluna 3, como passar na matéria.
    Os resultados esperados sempre devem estar na ultima Coluna.
    Ex de como seria inserido:
        PRISM = [ ['estuda', 'Nao_estuda'], ['fez_atividade', 'nao_fez_atividade'], ['passa', 'nao_passa'] ]
        Valor_esperado = 'passa'
        
    '''
# PRISM = [['moreno', 'loiro', 'loiro', 'moreno', 'ruivo', 'ruivo', 'grisalho'], ['alto', 'baixo', 'baixo', 'baixo', 'medio', 'medio', 'medio'], ['magro', 'magro', 'gordo', 'gordo', 'magro', 'gordo', 'gordo'], ['nao', 'talvez', 'nao', 'nao', 'nao', 'sim', 'sim']]
PRISM = [['Young', 'Young', 'Young', 'Young', 'Young', 'Young', 'Young', 'Young', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Pre-presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic', 'Presbyopic'], ['Myope', 'Myope', 'Myope', 'Myope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Myope', 'Myope', 'Myope', 'Myope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Myope', 'Myope', 'Myope', 'Myope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope', 'Hypermetrope'], ['Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'], ['Normal', 'Reduced', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal', 'Reduced', 'Normal'], ['Hard', 'None', 'None', 'Soft', 'None', 'Soft', 'None', 'Hard', 'None', 'Soft', 'None', 'Hard', 'None', 'Soft', 'None', 'None', 'None', 'None', 'None', 'Hard', 'None', 'Soft', 'None', 'None']]
valor_esperado = 'Hard'
Quantidade = list(list())
variaveis = []
aux = 0
aux2 = []
flag = 0

# Checa se as variaveis tem tamanhos iguais
checar(aux)


# Monta o cabeçalho
for c in range(len(PRISM)):
    variaveis.append('variavel ' + str(c+1))


# Função de DEBUG, para ver a tabela


while True:
    Quantidade.clear()
    tabela()
    funcao_quantidade(flag)
    min = estatisticas()
    if not 0 in aux2:
        break
    criando_regra()