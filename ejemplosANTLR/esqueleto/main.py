from antlr4 import *
from antlr.MayoParser import MayoParser
from antlr.MayoLexer import MayoLexer
from antlr.MayoListener import MayoListener

# elParser, elLexer, elListener serán generados a partir del .g4, importar arriba

class miListener(MayoListener):
    variables = {}
    def enterDec_entera(self, ctx: MayoParser.Dec_enteraContext):
        for x in ctx.SIMBOLO():
            if x.getText() in self.variables:
                raise Exception("Variable previamente declarada")
            self.variables[x.getText()] = 'entero'

class miListener2(MayoListener):
    def exitAdd(self, ctx:MayoParser.AddContext):
        if ctx.expresion(0).data_type != ctx.expresion(1).data_type:
            raise Exception("Tipos de datos no coinciden")
        ctx.data_type = ctx.expresion(0).data_type
    def enterNumber(self, ctx:MayoParser.NumberContext):
        ctx.data_type = 'entero'

    def enterVar(self, ctx:MayoParser.VarContext):
        if ctx.getText() not in self.variables:
            raise Exception("Variable no declarada previamente")
        ctx.data_type = self.variables[ctx.getText()]

class miListener3(MayoListener):
    funciones = {}
    def enterFuncion(self, ctx:MayoParser.FuncionContext):
        params = {}
        for p in ctx.parametro():
             params[p.SIMBOLO.getText()] = p.tipo.getText()
        self.funciones[ctx.SIMBOLO] = params

    def exitCall(self, ctx:MayoParser.CallContext):
        for e, p in zip(ctx.expresion(), self.funciones[ctx.SIMBOLO.getText()]):
            if e.data_type != p:
                raise Exception("Tipos de datos no coinciden")


def main():
    parser = MayoParser(CommonTokenStream(MayoLexer(FileStream('test.txt'))))

    tree = parser.program()

    walker = ParseTreeWalker()
    # Puedo hacer los recorridos con los listeners que quiera!

    walker.walk(miListener(), tree)
    #walker.walk(miListener(), tree)
    #walker.walk(miListener(), tree)

if __name__ == '__main__':
    main()