__author__ = 'leonardo.distasio & jeshon.assuncao'

import AST
from AST import addToClass

vars = {}

@addToClass(AST.ProgramNode)
def execute(self):
    for c in self.children:
        c.execute()

@addToClass(AST.TokenNode)
def execute(self):
    if isinstance(self.tok, str):
        try:
            return vars[self.tok]
        except KeyError:
            print("*** Error : variable %s undefined !" % self.tok)
    return self.tok

@addToClass(AST.AssignNode)
def execute(self):
    vars[self.children[0].tok] = self.children[1].execute()

if __name__ == "__main__":
    import sys
    from parser import parse

    prog = open(sys.argv[1]).read()
    ast = parse(prog)

    ast.execute()