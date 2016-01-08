__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.yacc as yacc
import AST
from lex import tokens

vars = {}
className = ""

def p_programme(p):
    """programme : CLASS expression parameters '{' statement '}'
                   | CLASS expression '{' statement '}' """
    global className
    className = p[2]
    if(p[4] == '{'):
        p[0] = AST.ProgramNode([p[2]] + p[5].children)
    else:
        p[0] = AST.ProgramNode([p[2]] + p[4].children)

def p_programme_empty(p):
    """programme : CLASS expression parameters '{' '}'
                   | CLASS expression '{' '}' """
    p[0] = AST.ProgramNode(p[2])

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

def p_statement(p):
    """statement : expression ';' statement"""
    p[0] = AST.StatementNode([p[1]] + p[3].children)

def p_statement_expression(p):
    """statement : expression
                  | assignation"""
    p[0] = AST.StatementNode(p[1])

def p_access(p):
    """expression : PUBLIC type
                    | PRIVATE type
                    | PROTECTED type """
    if(p[2] != None):
        p[0] = AST.DeclarationNode([AST.TokenNode(p[1]), p[2]])

def p_expression_type(p):
    """type : INT variable
            | INTEGER variable
            | FLOAT variable
            | STRING variable
            | DOUBLE variable
            | CHAR variable
            | CHARACTER variable
            | VOID variable"""
    p[0] = AST.TypeNode([AST.TokenNode(p[1]), p[2]])

def p_function_type(p):
    """type : INT function
            | FLOAT function
            | STRING function
            | DOUBLE function
            | CHAR function
            | VOID function"""

def p_expression_variable_terminal(p):
    """variable : IDENTIFIER ',' variable
                    | IDENTIFIER ';' statement
                    | IDENTIFIER ';'
                    | IDENTIFIER ',' type
                    | IDENTIFIER"""
    try:
        if(p[1] != None):
            p[0] = AST.VariableNode([AST.TokenNode(p[1])] + p[3].children)
    except:
        if(p[1] != None):
            p[0] = AST.VariableNode(AST.TokenNode(p[1]))

def p_function_declaration(p):
    """function : IDENTIFIER parameters bloc
                | IDENTIFIER parameters bloc expression
                | IDENTIFIER parameters ';' expression
                | IDENTIFIER parameters ';' """

def p_expression_condition_while(p):
    """parameters : '(' type ')'
                    | '(' ')'"""

def p_bloc_statement(p):
    """bloc : '{' statement '}'"""

def p_bloc_empty(p):
    """bloc : '{' '}'
              | '{' '}' expression"""
    try:
        p[0] = p[3]
    except:
        print("", end="")

def p_while_declaration(p):
    """statement : WHILE expression bloc"""

def p_statement_return(p):
    """expression : RETURN expression"""

def p_expression_className(p):
    """expression : IDENTIFIER"""
    p[0] = AST.TokenNode(p[1])

def p_expression_number(p):
    """expression : NUMBER
                    | NUMBER ';'
                    | NUMBER ';' statement
                    | NUMBER ',' statement"""
    p[0] = AST.TokenNode([p[1]])

def p_expression_identifier(p):
    """expression : IDENTIFIER ';'"""

def p_assignation(p):
    """assignation : IDENTIFIER '=' expression"""
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])

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