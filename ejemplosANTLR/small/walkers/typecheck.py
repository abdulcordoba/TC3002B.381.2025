from ejemplosANTLR.small.antlr.SmallListener import SmallListener
from ejemplosANTLR.small.antlr.SmallParser import SmallParser

INT = 0
BOOL = 1

class TypeException(Exception):
    pass

class TypecheckListener(SmallListener):
    def __init__(self, types):
        self.types = {}

    def exitNot(self, ctx):
        if self.types[ctx.getChild(1)] != BOOL:
            raise TypeException()
        else:
            self.types[ctx] = BOOL
    def exitInt(self, ctx:SmallParser.IntContext):
        self.types[ctx] = 'int'
    def exitString(self, ctx:SmallParser.StringContext):
        self.types[ctx] = 'string'
    def exitTrue(self, ctx:SmallParser.BoolDeclContext):
        self.types[ctx] = 'boolean'
    def exitAdd(self, ctx:SmallParser.AddContext):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == right:
            self.types[ctx] = left
        else:
            raise Exception("Tipos incompatibles")


    def exitSub(self, ctx:SmallParser.SubContext):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == right:
            self.types[ctx] = left
        else:
            raise Exception("Tipos incompatibles")