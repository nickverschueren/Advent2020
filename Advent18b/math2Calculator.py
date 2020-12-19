import sys
from antlr4 import *
from antlr4 import tree
from math2Lexer import math2Lexer
from math2Parser import math2Parser

class math2Calculator():
    def handleFile(self, expr):
        sum = 0
        for child in expr.expression():
            sum += self.handleExpression(child)
        return sum

    def handleExpression(self, expr):
        if (len(expr.children) == 0):
            return 0        
        value = 1
        for child in expr.addition():
            value *= self.handleAddition(child)
        return value

    def handleAddition(self, expr):
        value = 0
        if expr.atom():
            value = int(expr.children[0].getText())
        elif expr.paren_expression():
            value = self.handleParenExpression(expr.children[0])
        for child in expr.addition():
            parenValue = self.handleAddition(child)
            value += parenValue
        return value

    def handleParenExpression(self, expr):
        value = self.handleExpression(expr.children[1])
        return value

    def processFile(self, filename):
        input_stream = FileStream(filename)
        lexer = math2Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = math2Parser(stream)
        tree = parser.file()
        return self.handleFile(tree)
