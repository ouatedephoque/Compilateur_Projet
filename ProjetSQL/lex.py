__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.lex as lex

tokens = (
    'VARIABLE',
    'NAME_CLASS',
    'VISIBILITY',
    'CLASS',
    'TYPE'
)

literals = '();={}'

t_ignore = ' \t'

# Definition du lexeme VARIABLE
def t_VARIABLE(t):
    r'[A-Za-z_]\w*'
    return t

def t_NAME_CLASS(t):
    r'[A-Za-z_]\w*'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_TYPE(t):
    r'int|float|string'
    return t

# Definition du lexeme VISIBILITY
def t_VISIBILITY(t):
    r'protected|private|public'
    return t

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

