# Generated from math2.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\5\2\21\n\2\7\2\23\n\2\f\2\16\2\26\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\4\7\4%")
        buf.write("\n\4\f\4\16\4(\13\4\3\4\3\4\3\4\7\4-\n\4\f\4\16\4\60\13")
        buf.write("\4\5\4\62\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\2\2")
        buf.write("\b\2\4\6\b\n\f\2\2\2;\2\24\3\2\2\2\4\31\3\2\2\2\6\61\3")
        buf.write("\2\2\2\b\63\3\2\2\2\n\67\3\2\2\2\f9\3\2\2\2\16\20\5\4")
        buf.write("\3\2\17\21\7\t\2\2\20\17\3\2\2\2\20\21\3\2\2\2\21\23\3")
        buf.write("\2\2\2\22\16\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25")
        buf.write("\3\2\2\2\25\27\3\2\2\2\26\24\3\2\2\2\27\30\7\2\2\3\30")
        buf.write("\3\3\2\2\2\31\36\5\6\4\2\32\33\7\7\2\2\33\35\5\6\4\2\34")
        buf.write("\32\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37")
        buf.write("\5\3\2\2\2 \36\3\2\2\2!&\5\n\6\2\"#\7\6\2\2#%\5\6\4\2")
        buf.write("$\"\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\62\3\2\2")
        buf.write("\2(&\3\2\2\2).\5\b\5\2*+\7\6\2\2+-\5\6\4\2,*\3\2\2\2-")
        buf.write("\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\62\3\2\2\2\60.\3\2\2")
        buf.write("\2\61!\3\2\2\2\61)\3\2\2\2\62\7\3\2\2\2\63\64\7\4\2\2")
        buf.write("\64\65\5\4\3\2\65\66\7\5\2\2\66\t\3\2\2\2\678\5\f\7\2")
        buf.write("8\13\3\2\2\29:\7\3\2\2:\r\3\2\2\2\b\20\24\36&.\61")
        return buf.getvalue()


class math2Parser ( Parser ):

    grammarFileName = "math2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'+'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "LPAREN", "RPAREN", "PLUS", 
                      "TIMES", "DIV", "WS" ]

    RULE_file = 0
    RULE_expression = 1
    RULE_addition = 2
    RULE_paren_expression = 3
    RULE_atom = 4
    RULE_number = 5

    ruleNames =  [ "file", "expression", "addition", "paren_expression", 
                   "atom", "number" ]

    EOF = Token.EOF
    INTEGER=1
    LPAREN=2
    RPAREN=3
    PLUS=4
    TIMES=5
    DIV=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(math2Parser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(math2Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(math2Parser.ExpressionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(math2Parser.WS)
            else:
                return self.getToken(math2Parser.WS, i)

        def getRuleIndex(self):
            return math2Parser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file(self):

        localctx = math2Parser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==math2Parser.INTEGER or _la==math2Parser.LPAREN:
                self.state = 12
                self.expression()
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==math2Parser.WS:
                    self.state = 13
                    self.match(math2Parser.WS)


                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(math2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(math2Parser.AdditionContext)
            else:
                return self.getTypedRuleContext(math2Parser.AdditionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(math2Parser.TIMES)
            else:
                return self.getToken(math2Parser.TIMES, i)

        def getRuleIndex(self):
            return math2Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = math2Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.addition()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==math2Parser.TIMES:
                self.state = 24
                self.match(math2Parser.TIMES)
                self.state = 25
                self.addition()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(math2Parser.AtomContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(math2Parser.PLUS)
            else:
                return self.getToken(math2Parser.PLUS, i)

        def addition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(math2Parser.AdditionContext)
            else:
                return self.getTypedRuleContext(math2Parser.AdditionContext,i)


        def paren_expression(self):
            return self.getTypedRuleContext(math2Parser.Paren_expressionContext,0)


        def getRuleIndex(self):
            return math2Parser.RULE_addition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)




    def addition(self):

        localctx = math2Parser.AdditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_addition)
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [math2Parser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.atom()
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 32
                        self.match(math2Parser.PLUS)
                        self.state = 33
                        self.addition() 
                    self.state = 38
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            elif token in [math2Parser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.paren_expression()
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 40
                        self.match(math2Parser.PLUS)
                        self.state = 41
                        self.addition() 
                    self.state = 46
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paren_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(math2Parser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(math2Parser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(math2Parser.RPAREN, 0)

        def getRuleIndex(self):
            return math2Parser.RULE_paren_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen_expression" ):
                listener.enterParen_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen_expression" ):
                listener.exitParen_expression(self)




    def paren_expression(self):

        localctx = math2Parser.Paren_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paren_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(math2Parser.LPAREN)
            self.state = 50
            self.expression()
            self.state = 51
            self.match(math2Parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(math2Parser.NumberContext,0)


        def getRuleIndex(self):
            return math2Parser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = math2Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(math2Parser.INTEGER, 0)

        def getRuleIndex(self):
            return math2Parser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = math2Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(math2Parser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





