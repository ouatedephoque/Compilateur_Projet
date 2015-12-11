__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.yacc as yacc
import AST
from lex import tokens

vars = {}
className = ""

def p_programme(p):
    """programme : CLASS expression '{' expression '}' """
    global className
    className = p[2]
    p[0] = p[4]

def p_programme_empty(p):
    """programme : CLASS expression '{' '}' """
    global className
    className = p[2]
    p[0] = p[4]

def p_expression_visibility(p):
    """expression : PUBLIC expression
                    | PRIVATE expression
                    | PROTECTED expression """
    p[0] = AST.TokenNode(p[2])

def p_expression_type(p):
    """expression : INT expression
                    | FLOAT expression
                    | STRING expression """
    p[0] = AST.TokenNode(p[2])

def p_expression_variable_terminal(p):
    """expression : IDENTIFIER ';' expression
                    | IDENTIFIER ',' expression
                    | IDENTIFIER ';' """
    p[0] = AST.TokenNode(p[1])

"""def p_expression_attributes(p):
    expression : PUBLIC INT IDENTIFIER ';'
                    | PUBLIC FLOAT IDENTIFIER ';'
                    | PUBLIC STRING IDENTIFIER ';'
                    | PRIVATE INT IDENTIFIER ';'
                    | PRIVATE FLOAT IDENTIFIER ';'
                    | PRIVATE STRING IDENTIFIER ';'
                    | PROTECTED INT IDENTIFIER ';'
                    | PROTECTED FLOAT IDENTIFIER ';'
                    | PROTECTED STRING IDENTIFIER ';'
    vars[p[3]] = p[2]
    p[0] = AST.TokenNode(p[3])"""


def p_expression_className(p):
    """expression : IDENTIFIER"""
    p[0] = AST.TokenNode(p[1])


def p_definition(p):
    """definition : IDENTIFIER IDENTIFIER IDENTIFIER ';' definition
                    | IDENTIFIER IDENTIFIER IDENTIFIER ';'"""
    p[0] = p[5]


def parse(programme):
    return yacc.parse(programme)


def p_error(p):
    if p:
        print("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print("Sytax error: unexpected end of file!")


parser = yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    print("Class name : ", end="")
    print(className)
    print(vars)