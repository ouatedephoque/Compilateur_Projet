__author__ = 'leonardo.distasio & jeshon.assuncao'

import ply.yacc as yacc
import AST
from lex import tokens

vars = {}
className = ""

def p_programme(p):
    """programme : CLASS expression '{' statement '}' """
    global className
    className = p[2]
    p[0] = p[4]

def p_programme_empty(p):
    """programme : CLASS expression '{' '}' """
    global className
    className = p[2]
    p[0] = p[4]

def p_statement(p):
    """statement : expression ';' statement"""
    p[0] = AST.ProgramNode([p[1]])

def p_statement_expression(p):
    """statement : expression
                  | assignation"""
    p[0] = AST.TokenNode(p[1])

def p_expression_visibility(p):
    """expression : PUBLIC expression
                    | PRIVATE expression
                    | PROTECTED expression """
    p[0] = AST.TokenNode(p[2])

def p_expression_type(p):
    """expression : INT statement
                    | FLOAT statement
                    | STRING statement
                    | VOID statement"""
    p[0] = AST.TokenNode(p[2])

def p_expression_variable_terminal(p):
    """expression : IDENTIFIER ';' expression
                    | IDENTIFIER ',' expression
                    | IDENTIFIER ';' """
    p[0] = AST.ProgramNode([p[1]])

def p_expression_condition_while(p):
    """expression : '(' expression ')'
                    | '(' ')'"""

def p_bloc_statement(p):
    """bloc : '{' statement '}'
              | '{' statement '}' expression"""
    p[0] = AST.TokenNode(p[2])

def p_bloc_empty(p):
    """bloc : '{' '}'
              | '{' '}' expression"""

def p_function_declaration(p):
    """statement : IDENTIFIER expression bloc"""

def p_while_declaration(p):
    """statement : WHILE condition_while bloc"""

def p_for_declaration(p):
    """statement : FOR condition_for bloc"""

def p_while_condition(p):
    """condition_while : '(' while_control ')'"""

def p_for_condition(p):
    """condition_for : '(' for_control ')' statement
                        | '(' for_control ')'"""

def p_for_control(p):
    """for_control : assignation ';' expression_boucle ';' expression_for_inc"""

def p_for_expression_in(p):
    """expression_for_inc : expression1 operateurInc expression1"""

def p_for_expression1(p):
    """expression1 : IDENTIFIER
                    | NUMBER"""

def p_while_control(p):
    """while_control : expression_boucle"""

def p_boucle_expression(p):
    """expression_boucle : expression1 operateur expression1"""

def p_operateur(p):
    """operateur : '='
                    | '<'
                    | '>'
                    | '!'
                    | '=' operateur
                    | '<' operateur
                    | '>' operateur
                    | '!' operateur """

def p_operateur_for(p):
    """operateurInc : '+'
                    | '-'
                    | '/'
                    | '*'
                    | '='
                    | '+' operateurInc
                    | '-' operateurInc
                    | '/' operateurInc
                    | '*' operateurInc """

def p_expression_className(p):
    """expression : IDENTIFIER"""
    p[0] = AST.TokenNode(p[1])

def p_expression_number(p):
    """expression : NUMBER
                    | NUMBER ';' statement
                    | NUMBER ',' statement"""
    p[0] = AST.TokenNode(p[1])

def p_assignation(p):
    """assignation : IDENTIFIER '=' expression"""
    p[0] = AST.AssignNode([AST.TokenNode(p[1]),p[3]])

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