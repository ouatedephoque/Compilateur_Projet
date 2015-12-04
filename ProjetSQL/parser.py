__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.yacc as yacc
import AST
from lex import tokens

vars = {}

def p_programme(p):
    """programme : CLASS NAME_CLASS '{' definition '}'"""
    print("Coucou")
    p[0] = p[4]

#def p_programme_function(p):
    #"""programme : VISIBILITY TYPE VARIABLE'(' parameters ')' '{' function '}'"""

def p_definition(p):
    """definition : VISIBILITY TYPE VARIABLE ';' definition
                    | VISIBILITY TYPE VARIABLE ';'"""
    print("Coucou")
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