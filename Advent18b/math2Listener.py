# Generated from math2.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .math2Parser import math2Parser
else:
    from math2Parser import math2Parser

# This class defines a complete listener for a parse tree produced by math2Parser.
class math2Listener(ParseTreeListener):

    # Enter a parse tree produced by math2Parser#file.
    def enterFile(self, ctx:math2Parser.FileContext):
        pass

    # Exit a parse tree produced by math2Parser#file.
    def exitFile(self, ctx:math2Parser.FileContext):
        pass


    # Enter a parse tree produced by math2Parser#expression.
    def enterExpression(self, ctx:math2Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by math2Parser#expression.
    def exitExpression(self, ctx:math2Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by math2Parser#addition.
    def enterAddition(self, ctx:math2Parser.AdditionContext):
        pass

    # Exit a parse tree produced by math2Parser#addition.
    def exitAddition(self, ctx:math2Parser.AdditionContext):
        pass


    # Enter a parse tree produced by math2Parser#paren_expression.
    def enterParen_expression(self, ctx:math2Parser.Paren_expressionContext):
        pass

    # Exit a parse tree produced by math2Parser#paren_expression.
    def exitParen_expression(self, ctx:math2Parser.Paren_expressionContext):
        pass


    # Enter a parse tree produced by math2Parser#atom.
    def enterAtom(self, ctx:math2Parser.AtomContext):
        pass

    # Exit a parse tree produced by math2Parser#atom.
    def exitAtom(self, ctx:math2Parser.AtomContext):
        pass


    # Enter a parse tree produced by math2Parser#number.
    def enterNumber(self, ctx:math2Parser.NumberContext):
        pass

    # Exit a parse tree produced by math2Parser#number.
    def exitNumber(self, ctx:math2Parser.NumberContext):
        pass



del math2Parser