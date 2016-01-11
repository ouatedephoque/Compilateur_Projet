__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.lex as lex

reserved_words = (
    'private',
    'protected',
    'public',
    'class',
    'int',
    'Integer',
    'float',
    'string',
    'String',
    'char',
    'Character',
    'double',
    'while',
    'for',
    'extends',
    'implements',
    'print',
    'void',
    'return',
    'new',
    'if',
    'else'
)

tokens = (
    'IDENTIFIER',
    'NUMBER'
) + tuple(map(lambda s:s.upper(), reserved_words))

literals = '();={},!<>"\'/*+-'

t_ignore = ' \t'

# Definition du lexeme IDENTIFIER
def t_IDENTIFIER(t):
    r'[A-Za-z_]\w*'
    if(t.value in reserved_words):
        t.type = t.value.upper()
    return t

# Definition du lexeme NUMBER
def t_NUMBER(t):
    r'\d+\.?\d*'
    t.value = float(t.value)
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

