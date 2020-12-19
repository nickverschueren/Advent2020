# Generated from math1.g4 by ANTLR 4.9
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
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\5\2\r\n\2\7")
        buf.write("\2\17\n\2\f\2\16\2\22\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3\34\n\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\2\3\4\6\2\4\6\b\2\3\3\2\6\7\2)\2\20")
        buf.write("\3\2\2\2\4\33\3\2\2\2\6%\3\2\2\2\b\'\3\2\2\2\n\f\5\4\3")
        buf.write("\2\13\r\7\t\2\2\f\13\3\2\2\2\f\r\3\2\2\2\r\17\3\2\2\2")
        buf.write("\16\n\3\2\2\2\17\22\3\2\2\2\20\16\3\2\2\2\20\21\3\2\2")
        buf.write("\2\21\23\3\2\2\2\22\20\3\2\2\2\23\24\7\2\2\3\24\3\3\2")
        buf.write("\2\2\25\26\b\3\1\2\26\27\7\4\2\2\27\30\5\4\3\2\30\31\7")
        buf.write("\5\2\2\31\34\3\2\2\2\32\34\5\6\4\2\33\25\3\2\2\2\33\32")
        buf.write("\3\2\2\2\34\"\3\2\2\2\35\36\f\5\2\2\36\37\t\2\2\2\37!")
        buf.write("\5\4\3\6 \35\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#")
        buf.write("\5\3\2\2\2$\"\3\2\2\2%&\5\b\5\2&\7\3\2\2\2\'(\7\3\2\2")
        buf.write("(\t\3\2\2\2\6\f\20\33\"")
        return buf.getvalue()


class math1Parser ( Parser ):

    grammarFileName = "math1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'+'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "LPAREN", "RPAREN", "PLUS", 
                      "TIMES", "DIV", "WS" ]

    RULE_file = 0
    RULE_expression = 1
    RULE_atom = 2
    RULE_number = 3

    ruleNames =  [ "file", "expression", "atom", "number" ]

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
            return self.getToken(math1Parser.EOF, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(math1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(math1Parser.ExpressionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(math1Parser.WS)
            else:
                return self.getToken(math1Parser.WS, i)

        def getRuleIndex(self):
            return math1Parser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file(self):

        localctx = math1Parser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==math1Parser.INTEGER or _la==math1Parser.LPAREN:
                self.state = 8
                self.expression(0)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==math1Parser.WS:
                    self.state = 9
                    self.match(math1Parser.WS)


                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 17
            self.match(math1Parser.EOF)
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

        def LPAREN(self):
            return self.getToken(math1Parser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(math1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(math1Parser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(math1Parser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(math1Parser.AtomContext,0)


        def TIMES(self):
            return self.getToken(math1Parser.TIMES, 0)

        def PLUS(self):
            return self.getToken(math1Parser.PLUS, 0)

        def getRuleIndex(self):
            return math1Parser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = math1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [math1Parser.LPAREN]:
                self.state = 20
                self.match(math1Parser.LPAREN)
                self.state = 21
                self.expression(0)
                self.state = 22
                self.match(math1Parser.RPAREN)
                pass
            elif token in [math1Parser.INTEGER]:
                self.state = 24
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = math1Parser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 27
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 28
                    _la = self._input.LA(1)
                    if not(_la==math1Parser.PLUS or _la==math1Parser.TIMES):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 29
                    self.expression(4) 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(math1Parser.NumberContext,0)


        def getRuleIndex(self):
            return math1Parser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = math1Parser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
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
            return self.getToken(math1Parser.INTEGER, 0)

        def getRuleIndex(self):
            return math1Parser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = math1Parser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(math1Parser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




