# Instânciação do lex
import ply.lex as lex
import ply.yacc as yacc
from tabulate import *
from math import sqrt, log
import pprint


####################################
####################################
####################################

# Implementação da tabela Hash
class TabelaHash:

    # Método construtor
    def __init__(self):
        self.limite = 17
        self.array = [[] for i in range(self.limite)]

    # Método criado para classe
    def obter_hash(self, chave):

        # Variável utilizada para armazenar a soma
        ind = 0

        # Percorre os caracteres da variável
        for char in chave:
            # Recebe um valor inteiro que representa o Unicode do caractere
            ind += ord(char)

        # Retorna o resto da divisão da soma do(s) caractere(s) pelo valor limite que vai representar aonde está localizado na tabela (índice)
        return ind % self.limite

    # Métodos específicos do Python
    # Retorna o valor da chave que foi armazenada
    def __getitem__(self, chave):

        # Recebe o índice na tabela
        ind = self.obter_hash(chave)

        # Itera por todos os itens contidos no índice especificado
        for elemento in self.array[ind]:

            # Checa se a chave corresponde à passada
            if elemento[0] == chave:
                # Retorna o valor ligado a chave
                return elemento[1]

    def __setitem__(self, chave, valor):
        # Recebe o índice na tabela
        ind = self.obter_hash(chave)

        # Flag utlizado
        f_encontrou = False

        # Itera por todos os itens contidos no índice especificado
        # O enumerate retorna o índice do elemento atual que está sendo olhado, esse valor passará para variável indice
        for indice, elemento in enumerate(self.array[ind]):

            # Caso a variável já esteja inclusa na tabela

            # O tamanho do elemento caso esteja preenchido é 2, porque é o conteúdo da tupla (chave, valor)
            # Depois checa se a chave do elemento é a mesma da solicitada (para substituir o valor armazenado)
            if len(elemento) == 2 and elemento[0] == chave:
                # Substitui o valor antigo pelo novo de uma chave passada
                # ind: índice na tabela hash
                # indice: índice no array especificado da taebla
                self.array[ind][indice] = (chave, valor)

                # Altera o valor da flag
                f_encontrou = True
                break

        # Caso não ache a variável na tabela
        if not f_encontrou:
            # Adiciona o par chave,valor no índice h da tabela
            self.array[ind].append((chave, valor))


# LEXER

# Lista de tokens
# Similar aos %token do calc-master

reservadas = {
    'if': 'IF',
    'else': 'ELSE',
    'sqrt': 'SQRT',
    'log': 'LOG'
}

tokens = [
             'ID', 'NUMERO',
             'SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO', 'RESTO', 'POTENCIA',
             'IGUAL', 'EQ', 'NE', 'GT', 'LT', 'GE', 'LE', 'AND', 'OR',
             'SOMIGUAL', 'SUBIGUAL', 'MULIGUAL', 'DIVIGUAL', 'RESIGUAL',
             'LPAREN', 'RPAREN',
         ] + list(reservadas.values())

# Expressões regulares para os reconhecimento de padrões dos tokens
t_ignore = " \t"  # Ignorar espaço em branco
t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_RESTO = r'%'
t_POTENCIA = r'\^'
t_IGUAL = r'\='
t_SOMIGUAL = r'\+\='
t_SUBIGUAL = r'\-\='
t_MULIGUAL = r'\*\='
t_DIVIGUAL = r'\/\='
t_RESIGUAL = r'\%\='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_EQ = r'\=\='  # Equal - Igual a
t_NE = r'\!\='  # Not Equal - Diferente de
t_GT = r'\>'  # Greater than - Maior que
t_LT = r'\<'  # Lower than - Menor que
t_GE = r'\>\='  # Greater or Equal then - Maior ou igual a
t_LE = r'\<\='  # Lower or Equal then - Menor ou igual a
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'ID')
    return t


def t_NUMERO(t):
    r"[0-9]*[\.]?[0-9]+([e|E][-|+]?[0-9]+)?"

    if '.' in t.value or 'E' in t.value or 'e' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)

    return t


# Reconhecimento de erros ao gerar os tokens
# yyerror
def t_error(t):
    print(f"[ERRO] Erro léxico (caractere não reconhecido): {t.value[0]!r}")
    t.lexer.skip(1)


####################################
####################################
####################################

# YACC - Parser (Analisador sintático) (Similar ao BISON)

# Precedência para operações aritméticas
precedence = (
    ('nonassoc', 'EQ', 'NE', 'GT', 'LT', 'GE', 'LE'),  # Operações relacionais
    ('left', 'IF'),
    ('left', 'ELSE'),
    ('left', 'SOMA', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO', 'RESTO'),
    ('right', 'POTENCIA'),  # Assim como falado na aula (Calc-master)
    ('right', 'NEGATIVO'),
)

# Tabela de símbolos (Utilizando tabela hash)

hash = TabelaHash()


# Atribuição (usado para variáveis)
def p_termo_atribuicao(p):
    'termo : ID IGUAL expressao'
    hash[p[1]] = p[3]


def p_termo_oper_atribuicao(p):
    '''termo : ID SOMIGUAL expressao
           | ID SUBIGUAL expressao
           | ID MULIGUAL expressao
           | ID DIVIGUAL expressao
           | ID RESIGUAL expressao'''

    if hash[p[1]]:
        if p[2] == '+=':
            hash[p[1]] += p[3]
        elif p[2] == '-=':
            hash[p[1]] -= p[3]
        elif p[2] == '*=':
            hash[p[1]] *= p[3]
        elif p[2] == '/=':
            hash[p[1]] /= p[3]
        elif p[2] == '%=':
            hash[p[1]] %= p[3]
    else:
        print(f" [ERRO] Variável não reconhecida {p[1]!r}")
        p[0] = 0



# Printar expressão
def p_termo_expressao(p):
    '''termo : expressao
             | termo_if'''

    print(p[1])


def p_termo_if(p):
    '''termo_if : IF LPAREN comparacao RPAREN termo %prec IF
                | IF LPAREN comparacao RPAREN termo ELSE termo'''

    p[0] = p[3]

    # if p[3]:  # Se o resultado da comparação for True
    #     p[0] = p[3]
    # else:  # Se o resultado da comparação for False
    #     if p[7]:
    #         p[0] = p[3]


# Operações matemáticas
def p_expressao_operacoes(p):
    '''expressao : expressao SOMA expressao
                  | expressao SUBTRACAO expressao
                  | expressao MULTIPLICACAO expressao
                  | expressao DIVISAO expressao
                  | expressao RESTO expressao
                  | expressao POTENCIA expressao '''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]


def p_metodos_matematicos(p):
    '''expressao : SQRT LPAREN expressao RPAREN
                 | LOG LPAREN expressao RPAREN'''

    if p[1] == 'sqrt':
        p[0] = sqrt(p[3])
    elif p[1] == 'log':
        p[0] = log(p[3])


# Operações relacionais
def p_expressao_oprel(p):
    '''comparacao : expressao EQ expressao
                | expressao NE expressao
                | expressao GT expressao
                | expressao LT expressao
                | expressao GE expressao
                | expressao LE expressao
                | expressao EQ expressao AND comparacao
                | expressao EQ expressao OR comparacao
                | expressao NE expressao AND comparacao
                | expressao NE expressao OR comparacao
                | expressao GT expressao AND comparacao
                | expressao GT expressao OR comparacao
                | expressao LT expressao AND comparacao
                | expressao LT expressao OR comparacao
                | expressao GE expressao AND comparacao
                | expressao GE expressao OR comparacao
                | expressao LE expressao AND comparacao
                | expressao LE expressao OR comparacao
                '''

    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]


def p_expressao_negativo(p):
    # Precedencia especial
    # (Nem um token nem uma regra gramatical)
    'expressao : SUBTRACAO expressao %prec NEGATIVO'

    p[0] = -p[2]


# Uso de parênteses
def p_expressao_parenteses(p):
    'expressao : LPAREN expressao RPAREN'

    p[0] = p[2]


def p_expressao_numero(p):
    'expressao : NUMERO'
    p[0] = p[1]


def p_expressao_ID(p):
    'expressao : ID'

    if hash[p[1]]:
        p[0] = hash[p[1]]
    else:
        print(f" [ERRO] Variável não reconhecida {p[1]!r}")
        p[0] = 0

    # try:
    #     p[0] = hash[p[1]]
    #     # p[0] = ids[p[1]]
    # except LookupError:
    #     print(f" [ERRO] Variável não reconhecida {p[1]!r}")
    #     p[0] = 0


def p_error(p):
    try:
        print(f"[ERRO] Erro de sintaxe em {p.value!r}")
    except:
        print(f"[ERRO] Sintaxe incorreta")


####################################
####################################
####################################

# Input para cadeia de entrada

# print('*=' * 20)
lexer = lex.lex()  # Instancia e chama o método do lexer
parser = yacc.yacc()  # Instancia e chama o método do parser
while True:
    try:
        print('-=' * 20)
        s = input('Cadeia de entrada > ')
        print('-=' * 20)
    except EOFError:  # End of file - Fim do arquivo
        break

    lexer.input(s)
    tok_lex = []
    toks_lexs = []
    while True:
        # Lê o próximo caractere
        tok = lexer.token()

        if not tok: break

        # tok.type, tok.value, tok.line, tok.lexpos
        # Os primeiros argumentos são importantes para o reconhecimento do componente
        # Os últimos são as posições no texto de entrada

        tok_lex.append(tok.type)
        tok_lex.append(tok.value)
        toks_lexs.append(tok_lex[:])
        tok_lex.clear()
        # print(f"Token {cont + 1} - <{tok.type}, '{tok.value}'>")

    print(tabulate(toks_lexs, headers=["TOKEN", "LEXEMA"]))
    print('-=' * 20)

    print('Resultado do parser =', end=' ')
    parser.parse(s)
    print('-=' * 20)

    print(f'\nTabela de símbolos (hash): ')
    pprint.pprint([{num: value} for num, value in enumerate(hash.array)], width=20)
    print('-=' * 20)
    print('\n\n\n')
