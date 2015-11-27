__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.lex as lex

tokens = (
    'NUMBER',
    'ADD_OP',
    'MUL_OP',
    'VARIABLE',
    'VISIBIITY'
)

literals = '();={}'

t_ignore = ' \t'

def t_ADD_OP(t):
    r'\+|-'
    return t

def t_MUL_OP(t):
    r'\*|/'
    return t

# Definition du lexeme VARIABLE
def t_VARIABLE(t):
    r'[A-Za-z_]\w*'
    return t

# Definition du lexeme NUMBER et recuperation de leur valeur
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print ("Line %d: Problem while parsing %s!" % (t.lineno,t.value))
        t.value = 0
    return t

# Definition du lexeme VISIBIITY
def t_VISIBIITY(t):
    r'protected|private|public|class'
    return t;

# Garder la trace du no de ligne ou intervient le lexeme
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Gestion des erreurs
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construction de l'analyseur
lex.lex()

# Tests
if __name__ == "__main__":
    import sys
    prog = open(sys.argv[1]).read()

    lex.input(prog)

    while 1:
        tok = lex.token()

        if not tok: break

        print("line %d: %s(%s)" %(tok.lineno, tok.type, tok.value))

