__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.yacc as yacc
import AST
from lex import tokens

vars = {}
className = ""

def p_classe(p):
    """classe : CLASS classname parameters '{' programme '}'
                   | CLASS classname '{' programme '}' """
    if(p[4] == '{'):
        p[0] = AST.ProgramNode([p[2]] + p[5].children)
    else:
        p[0] = AST.ProgramNode([p[2]] + p[4].children)

def p_classe_empty(p):
    """classe : CLASS classname parameters '{' '}'
                   | CLASS classname '{' '}' """
    p[0] = AST.ProgramNode(AST.TokenNode(p[2]))

def p_classname(p):
    """classname : IDENTIFIER"""
    p[0] = AST.TokenNode(AST.TokenNode(p[1]))

def p_parameters(p):
    """parameters : EXTENDS extension
                    | IMPLEMENTS implementation"""
    p[0] = p[2]

def p_extension(p):
    """extension : IDENTIFIER parameters
                   | IDENTIFIER"""

def p_implementation(p):
    """implementation : IDENTIFIER ',' implementation
                        | IDENTIFIER"""

def p_programme_end(p):
    """programme : statement ';' """
    p[0] = AST.ProgramNode(p[1])

def p_programme(p):
    """programme : statement ';' programme"""
    p[0] = AST.ProgramNode([p[1]] + p[3].children)

def p_programme_end_bloc(p):
    """programme : statement"""
    p[0] = AST.ProgramNode(p[1])

def p_declaration(p):
    """declaration : PUBLIC type
                    | PRIVATE type
                    | PROTECTED type"""
    p[0] = AST.DeclarationNode([AST.TokenNode(p[1]), p[2]])

def p_type(p):
    """type : INT variable
            | INTEGER variable
            | FLOAT variable
            | STRING variable
            | DOUBLE variable
            | CHAR variable
            | CHARACTER variable
            | VOID variable"""
    p[0] = AST.TypeNode([AST.TokenNode(p[1]), p[2]])

def p_expression_variable_terminal(p):
    """variable : IDENTIFIER"""
    p[0] = AST.TokenNode(p[1])

def p_expression_variable_non_terminal(p):
    """variable : IDENTIFIER ',' variable"""

def p_programme_function(p):
    """function : declaration parametres bloc
                | declaration parametres bloc programme"""
    try:
        p[0] = p[4].children
    except:
        print("", end="")

def p_expression_condition_while(p):
    """parametres : '(' type ')'
                    | '(' ')'"""

def p_bloc_programme(p):
    """bloc : '{' programme '}'"""

def p_bloc_empty(p):
    """bloc : '{' '}'"""

def p_statement(p):
    """statement : declaration
                | assignation
                | function"""
    p[0] = p[1]

def p_assignation(p):
    """assignation : IDENTIFIER '=' expression"""

def p_expression_number(p):
    """expression : NUMBER"""

def p_while_declaration(p):
    """statement : WHILE expression bloc"""

def p_statement_return(p):
    """expression : RETURN expression"""

def compilParse(prog):
    return yacc.parse(prog)

def p_error(p):
    if p:
        print("Syntax error in line %d" % p.lineno)
        yacc.errok()
    else:
        print("Sytax error: unexpected end of file!")

parser = yacc.yacc(outputdir='generated')

if __name__ == "__main__":
    import sys
    import os

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog)
    print(result)

    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    graph.write_pdf(name)
    print ("wrote ast to ", name)