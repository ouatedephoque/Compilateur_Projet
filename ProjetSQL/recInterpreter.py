__author__ = 'leonardo.distasio & jeshon.assuncao'

import AST
from AST import addToClass
from parserJava import className

vars = {}
javaToSql = {
    'string' : {'len' : 255, 'type' : 'varchar'},
    'int' : {'len' : 11, 'type' : "int"},
    'integer' : {'len' : 11, 'type' : "int"},
    'float' : {'len' : 11, 'type' : "float"},
    'double' : {'len' : 11, 'type' : "double"},
    'boolean' : {'len' : 1, 'type' : "tinyint"}
}

fileName = className + '.sql'
codeSql = ""

@addToClass(AST.ProgramNode)
def execute(self):
    global fileName, codeSql
    for c in self.children:
        if isinstance(c, AST.DeclarationNode):
            c.execute()
        else:
            fileName = c.execute() + '.sql'
            codeSql = "CREATE TABLE " + c.execute() + "(\n"

@addToClass(AST.DeclarationNode)
def execute(self):
    for d in self.children:
        d.execute()

@addToClass(AST.TypeNode)
def execute(self):
    global codeSql
    actualType = None
    for tn in self.children:
        if isinstance(tn, AST.VariableNode):
            tn.execute(actualType)
        else:
            actualType = javaToSql[tn.execute().lower()]

@addToClass(AST.VariableNode)
def execute(self, type=None):
    global codeSql
    for v in self.children:
        if isinstance(v, AST.DeclarationNode):
            v.execute()
        else:
            codeSql = codeSql + "\t" + v.execute() + " " + type['type'] +"(" + str(type['len']) + "),\n"

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
    from parserJava import compilParse
    import sys

    prog = open(sys.argv[1]).read()
    ast = compilParse(prog)
    ast.execute()

    codeSql = codeSql[:-2]+"\n"
    codeSql += ');'

    print(codeSql)
    fileSql = open(fileName, 'w')
    fileSql.write(codeSql)