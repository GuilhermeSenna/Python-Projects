import sys

# Ponteiro lookahead inicializado com 0
lookahead = 0

# Inicializa a expressão infixa e posfixa
infixa = posfixa = ''

# variável para checar se chegou ao fim da expressão
finish = False

# Dígitos e variaveis
variaveis = ['a', 'b', 'c', 'd']
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def digito_variavel():
    global posfixa
    t = infixa[lookahead]
    match(t)
    posfixa += t


def checar_proximo_digito():
    global lookahead, infixa

    if lookahead + 1 > len(infixa):
        return False
    else:
        # Checa se é um dígito ou vírgula
        if infixa[lookahead] in digitos:
            return True
        elif infixa[lookahead] == ',':
            # Checa se há símbolos antes e após a vírgula
            # no digito_parenteses() já
            if lookahead - 1 < 0 or lookahead + 1 > len(infixa):
                return False
            else:
                return True
        else:
            return False


def digito_parenteses_virgula():
    global posfixa, lookahead, infixa

    # variavel: Permite apenas 1
    # digito: Permite digitos consecutivos (como 23 e 149)
    # vírgula: É adicionado caso existem símbolos anteriores e posteriores e sejam dígitos

    if lookahead_variaveis():
        digito_variavel()
    elif lookahead_digitos():
        digito_variavel()
        # Checar se o proximo símbolo EXISTE e é um dígito
        if checar_proximo_digito():
            digito_parenteses_virgula()
    elif igual_lookahead(','):

        # Checa antes se o símbolo anterior e posterior EXISTEM e são dígitos
        if checar_proximo_digito():
            digito_variavel()
            digito_parenteses_virgula()
    elif igual_lookahead('('):
        # Armazena o primeiro parênteses e retorna ao fluxo inicial para depois fechar o parênteses
        match('(')
        expressao()
        match(')')
    else:
        pass


def pot():
    global posfixa
    if igual_lookahead('^'):
        match('^')
        digito_parenteses_virgula()
        posfixa += '^'
    else:
        pass


def operando():
    digito_parenteses_virgula()
    pot()


def mul_div():
    global posfixa
    if igual_lookahead('*'):
        match('*')
        operando()
        posfixa += '*'
        mul_div()
    elif igual_lookahead('/'):
        match('/')
        operando()
        posfixa += '/'
        mul_div()
    else:
        pass


def operacao():
    operando()
    mul_div()


def som_sub():
    global posfixa
    if igual_lookahead('+'):
        match('+')
        operacao()
        posfixa += '+'
        som_sub()
    elif igual_lookahead('-'):
        match('-')
        operacao()
        posfixa += '-'
        som_sub()
    else:
        pass


def expressao():
    operacao()
    som_sub()


def match(t):
    if igual_lookahead(t):
        mover_lookahead()
    else:
        mostrar_erro_sintaxe()


# Checa se o símbolo passado como parâmero é igual ao que o lookahead está lendo
def igual_lookahead(t):
    # Impede o lookhead de olhar um caracterer além do tamanho da expressão infixa
    if lookahead >= len(infixa):
        return False
    elif infixa[lookahead] == t:
        return True
    else:
        return False


# Incrementar o lookahead
def mover_lookahead():
    global lookahead
    lookahead += 1

    # Chegou no último caractere
    if lookahead == len(infixa):
        global finish
        finish = True


# Checa se está apontando para os dígitos
def lookahead_digitos():
    # Impede de apontar para além do tamanho da expressão (estouro)
    if lookahead >= len(infixa) or finish:
        mostrar_erro_sintaxe()
    else:
        if infixa[lookahead] in digitos:
            return True
        else:
            return False


# Checa se está apontando para as variaveis
def lookahead_variaveis():
    # Impede de apontar para além do tamanho da expressão (estouro)
    if lookahead >= len(infixa) or finish:
        mostrar_erro_sintaxe()
    else:
        if infixa[lookahead] in variaveis:
            return True
        else:
            return False


def mostrar_erro_sintaxe():
    print(">> Erro de sintaxe")
    sys.exit()


# main function
def main():
    global infixa
    infixa = input("Entre a expressão infixa: ")

    # Chama o símbolo inicial
    expressao()

    # Se chegou ao final da execução mas a expressão infixa não foi toda processada
    if not finish:
        mostrar_erro_sintaxe()
    else:
        print('Posfixa:', posfixa)


main()