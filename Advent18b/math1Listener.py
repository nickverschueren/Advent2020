# Generated from math1.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .math1Parser import math1Parser
else:
    from math1Parser import math1Parser

# This class defines a complete listener for a parse tree produced by math1Parser.
class math1Listener(ParseTreeListener):

    # Enter a parse tree produced by math1Parser#file.
    def enterFile(self, ctx:math1Parser.FileContext):
        pass

    # Exit a parse tree produced by math1Parser#file.
    def exitFile(self, ctx:math1Parser.FileContext):
        pass


    # Enter a parse tree produced by math1Parser#expression.
    def enterExpression(self, ctx:math1Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by math1Parser#expression.
    def exitExpression(self, ctx:math1Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by math1Parser#atom.
    def enterAtom(self, ctx:math1Parser.AtomContext):
        pass

    # Exit a parse tree produced by math1Parser#atom.
    def exitAtom(self, ctx:math1Parser.AtomContext):
        pass


    # Enter a parse tree produced by math1Parser#number.
    def enterNumber(self, ctx:math1Parser.NumberContext):
        pass

    # Exit a parse tree produced by math1Parser#number.
    def exitNumber(self, ctx:math1Parser.NumberContext):
        pass



del math1Parser