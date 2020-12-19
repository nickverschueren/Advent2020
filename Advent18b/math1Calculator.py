import sys
from antlr4 import *
from antlr4 import tree
from math1Lexer import math1Lexer
from math1Parser import math1Parser

class math1Calculator():
    def handleFile(self, expr):
        sum = 0
        for child in expr.expression():
            sum += self.handleExpression(child)
        return sum

    def handleExpression(self, expr):
        if expr.LPAREN():
            return self.handleExpression(expr.children[1])
        adding = True
        value = 0
        for child in expr.getChildren():
            if expr.atom():
                value = int(expr.getText())
                break
            elif isinstance(child, tree.Tree.TerminalNode):
                adding = child.getText() == "+"
            else:
                parenValue = self.handleExpression(child)
                if adding:
                    value += parenValue
                else:
                    value *= parenValue
        return value
    
    def processFile(self, filename):
        input_stream = FileStream(filename)
        lexer = math1Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = math1Parser(stream)
        tree = parser.file()
        return self.handleFile(tree)
