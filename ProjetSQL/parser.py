__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.yacc as yacc
import AST
from lex import tokens

vars = {}

def p_programme(p):
    """programme : CLASS expression '{' expression '}' """
    print("Coucou")
    p[0] = p[4]

def p_expression_attributes(p):
    """expression : PUBLIC INT IDENTIFIER ';'
                    | PUBLIC FLOAT IDENTIFIER ';'
                    | PUBLIC STRING IDENTIFIER ';'
                    | PRIVATE INT IDENTIFIER ';'
                    | PRIVATE FLOAT IDENTIFIER ';'
                    | PRIVATE STRING IDENTIFIER ';'
                    | PROTECTED INT IDENTIFIER ';'
                    | PROTECTED FLOAT IDENTIFIER ';'
                    | PROTECTED STRING IDENTIFIER ';'"""
    p[0] = AST.TokenNode(p[3])

def p_expression_className(p):
    """expression : IDENTIFIER"""
    p[0] = AST.TokenNode(p[1])

def p_definition(p):
    """definition : IDENTIFIER IDENTIFIER IDENTIFIER ';' definition
                    | IDENTIFIER IDENTIFIER IDENTIFIER ';'"""
    print("Coucou2")
    p[0] = p[5]

def parse(programme):
    return yacc.parse(programme)

#def p_error(p):
    #print ("Syntax error in line %d" % p.lineno)
    #yacc.errok()

parser = yacc.yacc(outputdir='generated')

if __name__ == "__main__":
	import sys

	prog = open(sys.argv[1]).read()
	result = yacc.parse(prog)
	print (result)